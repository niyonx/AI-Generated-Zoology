dataDir=../data/sketch-img

python test_pretrained.py \
    --name pretrained \
    --dataset_mode test_dir \
    --dataroot ../data/raw-img/ \
    --results_dir ${dataDir}/ \
    --checkpoints_dir ./ \
    --model pix2pix \
    --which_direction AtoB \
    --norm batch \
    --input_nc 3 \
    --output_nc 1 \
    --which_model_netG resnet_9blocks \
    --no_dropout \
