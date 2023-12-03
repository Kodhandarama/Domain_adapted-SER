#!/bin/bash

#########################################################
# Set the directory path
#########################################################
corpus_dir=/home/eng/s/sxc220013/Documents/journal1/domain_adaptation_ser/MSP_podcast 
opensmile_dir=/home/eng/s/sxc220013/Documents/journal1/domain_adaptation_ser/opensmile-3.0.2-linux-x86_64
##########################################################
feature_dir=./feature/labeled
data_dir=./data/labeled
log_dir=./log
model_path=./model/ladder

################ Preprocess ################
# bash extract_feat.sh ${opensmile_dir}/config ${corpus_dir}/Audios ${feature_dir} || exit 1;
# python3 -u preprocess_hld.py $feature_dir data_pre/labeled || exit 1;
# python3 -u prepare_data.py data_pre/labeled ${data_dir} ${corpus_dir}/Labels/labels_consensus.json || exit 1;

#exit 1
#rm -rf data_pre

# # Run this scirpt if you have unlabeled dataset for training.
unlabel_dir=/home/eng/s/sxc220013/Documents/journal1/domain_adaptation_ser/unlabeled_dataset  # Make sure that all unlabeled wav files are in this folder and sampled with 16kHz.
unlabel_feature_dir=./feature/unlabeled 
unlabel_data_dir=./data/unlabeled

# bash extract_unlabel.sh ${opensmile_dir}/config ${unlabel_dir} ./${unlabel_feature_dir} || exit 1;
# python3 -u preprocess_hld.py ${unlabel_feature_dir} data_pre/unlabeled || exit 1;
# python3 -u prepare_unlabel.py data_pre/unlabeled ${unlabel_data_dir} || exit 1;
# rm -rf data_pre


################ Training ################
mkdir -p $log_dir
# Training model with supervised dataset
# python3 -u train_ladder.py --norm_type=2 --net_type=ladder --task_type=STL \
#     --model_path=${model_path} --seed=0 > ${log_dir}/train_log.txt || exit 1;
# Training model with supervised & unsupervised dataset
 python3 -u train_ladder.py --norm_type=2 --net_type=ladder --task_type=STL \
    --model_path=${model_path} --seed=0 --use_unlabel > ${log_dir}/train_log.txt || exit 1;
    
################ Evaluation ################
 python3 -u eval_ladder.py --norm_type=2 --net_type=ladder --task_type=STL \
     --model_path=${model_path} > ${log_dir}/eval_log.txt|| exit 1;