import json
import csv
import os

def merge_split_to_csv(split_folder, split_name, out_dir):
    # gom 2 file human + augmented
    human_file = os.path.join(split_folder, f"{split_name}_human.json")
    aug_file = os.path.join(split_folder, f"{split_name}_augmented.json")

    all_data = []
    for jf in [human_file, aug_file]:
        with open(jf, "r", encoding="utf-8") as f:
            all_data.extend(json.load(f))

    out_csv = os.path.join(out_dir, f"{split_name}.csv")
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Input", "Output", "Image Index", "Question ID"])

        qid = 0
        for item in all_data:
            query = item["query"]
            output = item["label"]
            # lấy số trong imgname (two_col_103562.png -> 103562)
            img_index = int(os.path.splitext(item["imgname"])[0].split("_")[-1])
            writer.writerow([query, output, img_index, qid])
            qid += 1

    print(f"✅ Saved {out_csv} with {len(all_data)} samples.")


def main():
    root = "/home/godminhkhoa/Desktop/DATH/ChartQA/ChartQA Dataset"
    out_dir = "/home/godminhkhoa/Desktop/DATH/ChartQA/Data Extraction"
    os.makedirs(out_dir, exist_ok=True)

    for split in ["train", "val", "test"]:
        merge_split_to_csv(os.path.join(root, split), split, out_dir)


if __name__ == "__main__":
    main()
