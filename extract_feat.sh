#!/bin/bash

##############################################################
# Make sure that the opensmile is installed in your machine. #
##############################################################

OpenSmileConfigPath=$1 #/home/kyunster/Lib/opensmile/config
corpus_dir=$2 #/media/kyunster/hdd/corpus/MSP_Podcast_1.8/16kHz

hld_path=$3

find ${corpus_dir} -name "*.wav" > filelist.txt
filelist=( $( cat filelist.txt ))

mkdir -p $hld_path

for wav_path in ${filelist[@]};
do
    fname=`echo $wav_path | rev | awk '{split($0,a,"/"); print a[1]}' | rev`
    oname=`echo $fname | awk '{split($0,a,"."); print a[1]}'`.txt
    echo $fname

    full_path_wav_path=$(realpath "$wav_path")
    full_path_hld_path=$(realpath "$hld_path")
    full_path_oname=$(realpath "$oname")

    if [ ! -f ${hld_path}/${oname} ]; then
        cd /home/eng/s/sxc220013/Documents/journal1/domain_adaptation_ser/opensmile-3.0.2-linux-x86_64/bin/
       ./SMILExtract -C $OpenSmileConfigPath/is09-13/IS13_ComParE.conf -I $full_path_wav_path -O ${full_path_hld_path}/${oname} -l 0 || exit 1;
        cd -
    fi    
done

rm filelist.txt