## Set up the virtual environment in Google Colab

### Step-1: In Colab, clone the GitHub repo for the neural body

!git clone https://github.com/ppathi3/neuralbody

### Step-2: Installing required dependencies in Colab
```

# make sure that the PyTorch cuda is consistent with the environment cuda
# e.g., if your environment cuda is 11.8, install torch 2.1 built from cuda 11.8
a) install torch
!pip install torch==2.1.0+cu118 -f https://download.pytorch.org/whl/torch_stable.html

b) install project requirements
!pip install -r requirements.txt

c) install spconv
%cd spconv
%cd dist
!pip install spconv-1.2.1-cp36-cp36m-linux_x86_64.whl

# Note: Sometimes errors occur in Pillow and ImageIO libraries, if yes, use the below lines to update the libraries and resolve those errors

!pip install --upgrade pillow
!pip install imageio==2.4.0
```

### Step-3: Set up datasets

#### People-Snapshot dataset

1. Download the People-Snapshot dataset [here](https://graphics.tu-bs.de/people-snapshot).
2. Process the People-Snapshot dataset using the [script](https://github.com/zju3dv/neuralbody#process-people-snapshot).
3. Create a soft link:
    ```
    ROOT=/path/to/neuralbody
    cd $ROOT/data
    ln -s /path/to/people_snapshot people_snapshot
    ```

#### ZJU-Mocap dataset

1. If someone wants to download the ZJU-Mocap dataset, please fill in the [agreement](https://pengsida.net/project_page_assets/files/ZJU-MoCap_Agreement.pdf), and email me (pengsida@zju.edu.cn) and cc Xiaowei Zhou (xwzhou@zju.edu.cn) to request the download link.
2. Create a soft link:
    ```
    ROOT=/path/to/neuralbody
    cd $ROOT/data
    ln -s /path/to/zju_mocap zju_mocap
    ```


#### Once the above steps are done and the environment is set up, you can go back to the Readme file to download the pre-trained models and put them in the required directory before running the evaluation and visualization commands.

#### Downloading huge datasets/pre-trained models and loading them on Colab is not possible, we faced issues with the same. So it is better to mount the drive files add the neural body repo to the drive and directly upload the dataset files wherever required instead of doing it from Colab

```
Steps for mounting the neural body after adding it to drive

from google.colab import drive
drive.mount('/content/drive', force_remount=True)
%cd drive/MyDrive/neuralbody

```