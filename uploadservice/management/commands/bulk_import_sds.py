import os
import re
from datetime import datetime
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand
from uploadservice.models import UploadedFile

IGNORED_FOLDERS = {"old", "archive", "work in progress"}
DATE_PATTERN = re.compile(r"\d{6,8}")  # Matches MMDDYY or MMDDYYYY

class Command(BaseCommand):
    help = 'Import SDS files recursively. Supports hyphenated chemNos, flexible filenames, and skips duplicates.'

    def add_arguments(self, parser):
        parser.add_argument("root_folder", type=str, help="Path containing folders/files to import")

    def handle(self, *args, **options):
        root_folder = options["root_folder"]
        kind = "sdsFile"
        inserted = skipped = failed = 0

        for dirpath, dirnames, filenames in os.walk(root_folder):
            dirnames[:] = [
                d for d in dirnames if d.lower().strip() not in {f.lower() for f in IGNORED_FOLDERS}
            ]
            chem_no = os.path.basename(dirpath).strip()

            # ✅ ChemNo must be "2xxxx" or "10-something"
            if not (
                re.fullmatch(r"2\d{4}", chem_no) or
                re.fullmatch(r"10-[\w\-]+", chem_no) or
                re.fullmatch(r"26-[\w\-]+", chem_no)
            ):
                self.stdout.write(self.style.WARNING(
                    f"[Invalid chemNo] Skipping folder: {chem_no}"
                ))
                skipped += 1
                continue


            for file in filenames:
                if not file.lower().endswith((".pdf", ".doc", ".docx", ".xls", ".xlsx")):
                    skipped += 1
                    continue

                local_file_path = os.path.join(dirpath, file)
                base_name, ext = os.path.splitext(file)

                brand_name, raw_date = None, None
                parts = re.split(r"[_\-]", base_name)
                potential_date = parts[-1] if parts else ""

                if DATE_PATTERN.fullmatch(potential_date):
                    brand_parts = parts[:-1]
                    raw_date = potential_date
                else:
                    brand_parts = parts

                brand_name = " ".join(brand_parts).strip()

                try:
                    if raw_date:
                        raw_date = re.sub(r"[^\d]", "", raw_date)
                        parsed_date = datetime.strptime(raw_date, "%m%d%Y") if len(raw_date) == 8 else datetime.strptime(raw_date, "%m%d%y")
                        date = parsed_date.strftime("%Y-%m-%d")
                    else:
                        date = datetime.today().strftime("%Y-%m-%d")
                        self.stdout.write(self.style.WARNING(
                            f"[No date in filename] Using today's date for: {file}"
                        ))
                except Exception as e:
                    self.stdout.write(self.style.WARNING(
                        f"[Invalid date format] File: {file} | Raw: {raw_date or 'None'} | ChemNo: {chem_no}"
                    ))
                    skipped += 1
                    continue

                if UploadedFile.objects.filter(folder=chem_no, brand_name=brand_name).exists():
                    self.stdout.write(self.style.WARNING(
                        f"[Duplicate] Skipped (chemNo + brand): {file}"
                    ))
                    skipped += 1
                    continue

                sds_folder = os.path.join(settings.MEDIA_ROOT, "chemicalUploads", chem_no, "sds")
                os.makedirs(sds_folder, exist_ok=True)
                final_file_name = f"{brand_name.replace(' ', '_')}_{date}{ext}"
                target_path = os.path.join(sds_folder, final_file_name)

                try:
                    with open(local_file_path, "rb") as f:
                        default_storage.save(target_path, ContentFile(f.read()))

                    UploadedFile.objects.create(
                        folder=chem_no,
                        brand_name=brand_name,
                        date=date,
                        kind=kind,
                        file_name=final_file_name,
                        filepath=target_path
                    )
                    inserted += 1
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Failed to upload {file}: {e}"))
                    failed += 1

        self.stdout.write(self.style.SUCCESS(
            f"Done. Inserted: {inserted}, Skipped: {skipped}, Failed: {failed}"
        ))
