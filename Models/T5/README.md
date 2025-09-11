
This repo is adapted from [Transformers-T5](https://github.com/huggingface/transformers/tree/main/examples/pytorch)
# Training the T5 Model

In order to train the T5 model on any ChartQA dataset, you need to: 
* Prepare the training, validation, and test csv files (e.g., [example-csv-file](https://github.com/vis-nlp/ChartQA/blob/main/Figures%20and%20Examples/T5%20and%20VL-T5%20Input%20File%20Examples.csv)). The Input Column should contain the question and flatenned data table. The Output colum should contain the final answer. 
* Run the following command with your prefered hyperparameters.

```
python /home/godminhkhoa/Desktop/DATH/ChartQA/Models/T5/run_T5.py \
  --model_name_or_path t5-base \
  --do_train \
  --do_eval \
  --do_predict \
  --train_file "/home/godminhkhoa/Desktop/DATH/ChartQA/Data Extraction/train.csv" \
  --validation_file "/home/godminhkhoa/Desktop/DATH/ChartQA/Data Extraction/val.csv" \
  --test_file "/home/godminhkhoa/Desktop/DATH/ChartQA/Data Extraction/test.csv" \
  --text_column Input \
  --summary_column Output \
  --source_prefix "" \
  --output_dir /home/godminhkhoa/Desktop/DATH/ChartQA/output \
  --per_device_train_batch_size=8 \
  --per_device_eval_batch_size=16 \
  --predict_with_generate \
  --learning_rate 1e-4 \
  --num_beams 4 \
  --num_train_epochs 5 \
  --save_steps 500 \
  --eval_steps 500 \
  --eval_strategy steps \
  --save_strategy steps \
  --load_best_model_at_end \
  --overwrite_output_dir \
  --max_source_length 512
```



# Prediction
You need to first prepare the test dataset file as mentioned above (e.g., [example-csv-file](https://github.com/vis-nlp/ChartQA/blob/main/Figures%20and%20Examples/T5%20and%20VL-T5%20Input%20File%20Examples.csv)). Then, you can run the following command

```
!python -m torch.distributed.run --nproc_per_node 1 run_T5.py \
--model_name_or_path path-to-checkpoint/ \
--do_predict \
--test_file path-to-file.csv \
--text_column Input \
--summary_column Output \
--source_prefix "" \
--output_dir path-to-output/ \
--per_device_eval_batch_size=192 \
--predict_with_generate=True \
--max_source_length=1024
```

 <strong>Note:</strong> The metric in this [run_T5.py](https://github.com/vis-nlp/ChartQA/blob/main/Models/T5/run_T5.py) file is the exact accuracy which is different from the relaxed accuracy measure described in the paper. Hence, you will still need to evaluate the generated predictions using the relaxed accuracy. 
