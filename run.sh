python run.py \
--model_name_or_path klue/roberta-base \
--do_train \
--learning_rate 5e-5 \
--num_train_epochs 10 \
--output_dir output/baseline \
--per_gpu_eval_batch_size=16 \
--per_device_train_batch_size=16 \
--overwrite_output \
--train_file data/train.json \
