# Neural Body: Implicit Neural Representations with Structured Latent Codes for Novel View Synthesis of Dynamic Humans
### [Project Page](https://zju3dv.github.io/neuralbody) | [Video](https://www.youtube.com/watch?v=BPCAMeBCE-8) | [Journal Paper](https://ieeexplore.ieee.org/document/10045794) | [Conference Paper](https://arxiv.org/pdf/2012.15838.pdf) | [Data](https://github.com/zju3dv/neuralbody/blob/master/INSTALL.md#zju-mocap-dataset)

![monocular](https://zju3dv.github.io/neuralbody/images/monocular.gif)

> [Neural Body: Implicit Neural Representations with Structured Latent Codes for Novel View Synthesis of Dynamic Humans](https://arxiv.org/pdf/2012.15838.pdf)  
> Sida Peng, Yuanqing Zhang, Yinghao Xu, Qianqian Wang, Qing Shuai, Hujun Bao, Xiaowei Zhou  
> CVPR 2021

> [Implicit Neural Representations with Structured Latent Codes for Human Body Modeling](https://ieeexplore.ieee.org/document/10045794)  
> Sida Peng, Chen Geng, Yuanqing Zhang, Yinghao Xu, Qianqian Wang, Qing Shuai, Hujun Bao, Xiaowei Zhou  
> TPAMI 2023

## Installation

Please see [INSTALL.md](INSTALL.md) for manual installation.

## Run the code on People-Snapshot

Please see [INSTALL.md](INSTALL.md) to download the dataset.

We provide the pretrained models at [here](https://drive.google.com/drive/folders/1yR2KauFaM7kvQgsdlS_qsj9u9Y9qu9C-?usp=sharing).

### Process People-Snapshot

We already provide some processed data. If you want to process more videos of People-Snapshot, you could use [tools/process_snapshot.py](tools/process_snapshot.py).

You can also visualize smpl parameters of People-Snapshot with [tools/vis_snapshot.py](tools/vis_snapshot.py).

### Visualization on People-Snapshot

Take the visualization on `female-3-casual` as an example. The command lines for visualization are recorded in [visualize.sh](visualize.sh).

1. Download the corresponding pretrained model and put it to `$ROOT/data/trained_model/if_nerf/female3c/latest.pth`.
2. Visualization:
    * Visualize novel views of single frame
    ```
    python run.py --type visualize --cfg_file configs/snapshot_exp/snapshot_f3c.yaml exp_name female3c vis_novel_view True num_render_views 144
    ```

    ![monocular](https://zju3dv.github.io/neuralbody/images/monocular_render.gif)
    
    This is a time consuming operation, it takes a minimum of 3-4 hours to be executed successfully.
    After running this command, multiple images are generated in the *data/render* folder for the given pose in people snapshot using which the above visualization is generated.

    * Visualize views of dynamic humans with fixed camera
    ```
    python run.py --type visualize --cfg_file configs/snapshot_exp/snapshot_f3c.yaml exp_name female3c vis_novel_pose True
    ```

    ![monocular](https://zju3dv.github.io/neuralbody/images/monocular_perform.gif)

    * Visualize mesh
    ```
    # generate meshes
    python run.py --type visualize --cfg_file configs/snapshot_exp/snapshot_f3c.yaml exp_name female3c vis_mesh True train.num_workers 0
    # visualize a specific mesh
    python tools/render_mesh.py --exp_name female3c --dataset people_snapshot --mesh_ind 226
    ```

    ![monocular](https://zju3dv.github.io/neuralbody/images/monocular_mesh.gif)

3. The results of visualization are located at `$ROOT/data/render/female3c` and `$ROOT/data/perform/female3c`.


## Run the code on ZJU-MoCap

Please see [INSTALL.md](INSTALL.md) to download the dataset.

We provide the pretrained models at [here](https://drive.google.com/drive/folders/1yR2KauFaM7kvQgsdlS_qsj9u9Y9qu9C-?usp=sharing).

### Test on ZJU-MoCap

The command lines for test are recorded in [test.sh](test.sh).

Take the test on `sequence 313` as an example.

1. Download the corresponding pretrained model and put it to `$ROOT/data/trained_model/if_nerf/xyzc_313/latest.pth`.

2. Test on training human poses:
    ```
    python run.py --type evaluate --cfg_file configs/zju_mocap_exp/latent_xyzc_313.yaml exp_name xyzc_313
    ```
3. Test on unseen human poses:
    ```
    python run.py --type evaluate --cfg_file configs/zju_mocap_exp/latent_xyzc_313.yaml exp_name xyzc_313 test_novel_pose True
    ```

### Visualization on ZJU-MoCap

Take the visualization on `sequence 313` as an example. The command lines for visualization are recorded in [visualize.sh](visualize.sh).

1. Download the corresponding pretrained model and put it to `$ROOT/data/trained_model/if_nerf/xyzc_313/latest.pth`.
2. Visualization:
    * Visualize novel views of single frame
    ```
    python run.py --type visualize --cfg_file configs/zju_mocap_exp/latent_xyzc_313.yaml exp_name xyzc_313 vis_novel_view True
    ```
    ![zju_mocap](https://zju3dv.github.io/neuralbody/images/zju_mocap_render_313.gif)

    * Visualize novel views of single frame by rotating the SMPL model
    ```
    python run.py --type visualize --cfg_file configs/zju_mocap_exp/latent_xyzc_313.yaml exp_name xyzc_313 vis_novel_view True num_render_views 100
    ```
    ![zju_mocap](https://zju3dv.github.io/neuralbody/images/rotate_smpl.gif)

    * Visualize views of dynamic humans with fixed camera
    ```
    python run.py --type visualize --cfg_file configs/zju_mocap_exp/latent_xyzc_313.yaml exp_name xyzc_313 vis_novel_pose True num_render_frame 1000 num_render_views 1
    ```
    ![zju_mocap](https://zju3dv.github.io/neuralbody/images/zju_mocap_perform_fixed_313.gif) 

    * Visualize views of dynamic humans with rotated camera
    ```
    python run.py --type visualize --cfg_file configs/zju_mocap_exp/latent_xyzc_313.yaml exp_name xyzc_313 vis_novel_pose True num_render_frame 1000
    ```
    ![zju_mocap](https://zju3dv.github.io/neuralbody/images/zju_mocap_perform_313.gif)

    * Visualize mesh
    ```
    # generate meshes
    python run.py --type visualize --cfg_file configs/zju_mocap_exp/latent_xyzc_313.yaml exp_name xyzc_313 vis_mesh True train.num_workers 0
    # visualize a specific mesh
    python tools/render_mesh.py --exp_name xyzc_313 --dataset zju_mocap --mesh_ind 0
    ```
    ![zju_mocap](https://zju3dv.github.io/neuralbody/images/zju_mocap_mesh.gif)

4. The results of visualization are located at `$ROOT/data/render/xyzc_313` and `$ROOT/data/perform/xyzc_313`.

## To run the streamlit app

!pip install streamlit
# Get IP address for current virtual environment: Use this IP address as an input to the tunnel created by npx in next steps to access the application
!wget -q -O - ipv4.icanhazip.com
!pip install streamlit_option_menu
# To run the app file in a given port
!streamlit run app.py & npx localtunnel --port 8501

Click on the link generated by above command and paste the IP address, you'll find the application up and running.

![Screenshot (144)](https://github.com/ppathi3/neuralbody/assets/147741650/7608ab91-cde4-4d8e-af79-da9058262650)
![Screenshot (145)](https://github.com/ppathi3/neuralbody/assets/147741650/1362351d-0323-4749-b677-19a7bb7865cc)
![Screenshot (146)](https://github.com/ppathi3/neuralbody/assets/147741650/2d0f8986-8235-42b3-9d72-fc4a4ad66e7c)
![Screenshot (147)](https://github.com/ppathi3/neuralbody/assets/147741650/ca569248-ee5b-4061-8253-4be02aa47215)

## Citation

```
@article{peng2023implicit,
  title={Implicit Neural Representations with Structured Latent Codes for Human Body Modeling},
  author={Peng, Sida and Geng, Chen and Zhang, Yuanqing and Xu, Yinghao and Wang, Qianqian and Shuai, Qing and Zhou, Xiaowei and Bao, Hujun},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year={2023},
  publisher={IEEE}
}

@inproceedings{peng2021neural,
  title={Neural Body: Implicit Neural Representations with Structured Latent Codes for Novel View Synthesis of Dynamic Humans},
  author={Peng, Sida and Zhang, Yuanqing and Xu, Yinghao and Wang, Qianqian and Shuai, Qing and Bao, Hujun and Zhou, Xiaowei},
  booktitle={CVPR},
  year={2021}
}
```
