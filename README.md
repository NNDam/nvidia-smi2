# nvidia-smi2

A tool for enriching the output of nvidia-smi.

<a href="https://pypi.org/project/nvidia-smi2/"><img alt="Alt text" src="https://img.shields.io/badge/PyPI-3775A9.svg?style=for-the-badge&logo=PyPI&logoColor=white"/></a>

## Usage

Install

    pip install nvidia-smi2
    
Run

    nvidia-smi2 [-l [length]] [-u [username]]
      print GPU utilization with usernames and CPU stats for each GPU-utilizing process

      -l|--command-length [length]     Print longer part of the commandline. If `length'
                                       is provided, use it as the commandline length,
                                       otherwise print first 100 characters.
      -c|--color                       Colorize the output (green - free GPU, yellow -
                                       moderately used GPU, red - fully used GPU)
      -u|--user                        Name of user to summarize

Or run from src

    pip install termcolor
    chmod a+x nvidia-htop.py
    ./nvidia-htop.py [-l [length]] [-u [username]]
      print GPU utilization with usernames and CPU stats for each GPU-utilizing process

      -l|--command-length [length]     Print longer part of the commandline. If `length'
                                       is provided, use it as the commandline length,
                                       otherwise print first 100 characters.
      -c|--color                       Colorize the output (green - free GPU, yellow -
                                       moderately used GPU, red - fully used GPU)
      -u|--user                        Name of user to summarize

Note: for backward compatibility, `nvidia-smi | ./nvidia-htop.py [-l [length]] [-u [username]]` is also supported.

Note: running inside a container (docker, singularity, ...), `nvidia-smi` can only see processes running in the container.

## Example output
```
rnd@rnd:~$ nvidia-smi2 -l
Wed Jul 12 10:41:16 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.57.02    Driver Version: 470.57.02    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  On   | 00000000:01:00.0 Off |                  N/A |
| 55%   73C    P2    88W / 280W |   3248MiB / 11176MiB |     64%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  NVIDIA GeForce ...  On   | 00000000:02:00.0 Off |                  N/A |
| 59%   67C    P2    91W / 280W |   9397MiB / 11178MiB |      7%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  GPU   PID     USER    GPU MEM  %CPU  %MEM      TIME  COMMAND                                                                                               |
|    0  1242     root       9MiB   0.0   0.0  175 days  /usr/lib/xorg/Xorg vt1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  |
|    0  1966      gdm       4MiB   0.0   0.0  175 days  /usr/bin/gnome-shell                                                                                  |
|    0  6963  anonym1    2365MiB   2.9   3.1    7 days  python train.py                                                                                       |
|    0  8200     root     135MiB   0.1   0.4  117 days  python3 app.py xxxxxxxxx                                                                              |
|    0 12474      rnd     135MiB   0.1   0.8   11 days  python3 main.py xxxxxxxxxxx                                                                           |
|    0 19369     root     455MiB  62.4   2.5   20 days  python3 read_rtsp.py --path_stream xxxxxxxxxxxxxxxxxx                                                 |
|    0 30502     root     135MiB   0.0   1.8  16:24:10  python build_index.py                                                                                 |
|    1  1242     root       4MiB   0.0   0.0  175 days  /usr/lib/xorg/Xorg vt1 -displayfd 3 -auth xxxxxxx                                                     |
|    1 19422     root     455MiB  86.7   3.7   20 days  python3 read_rtsp.py --path_stream xxxxxxxxxxxxxxxxxxxxxxx                                            |
|    1 25255  anonym2    6917MiB   128   4.3  22:30:29  python train_image_classifier.py xxxx                                                                 |
|    1 27877     root    2017MiB   9.4   1.4   15 days  python consumer.py                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      USER    TOTAL GPU MEM  TOTAL %CPU  TOTAL %MEM  |
+-----------------------------------------------------+
|      root          3210MiB       158.6         9.8  |
|       gdm             4MiB         0.0         0.0  |
|   anonym1          2365MiB         2.9         3.1  |
|       rnd           135MiB         0.1         0.8  |
|   anonym2          6917MiB       128.0         4.3  |
+-----------------------------------------------------+
```

```
rnd@rnd:~$ nvidia-smi2 -l -u root
Wed Jul 12 10:51:06 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.57.02    Driver Version: 470.57.02    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  On   | 00000000:01:00.0 Off |                  N/A |
| 58%   69C    P2   106W / 280W |   3248MiB / 11176MiB |      5%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  NVIDIA GeForce ...  On   | 00000000:02:00.0 Off |                  N/A |
| 59%   65C    P2    80W / 280W |   9397MiB / 11178MiB |      7%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  GPU   PID     USER    GPU MEM  %CPU  %MEM      TIME  COMMAND                                                                                               |
|    0  1242     root       9MiB   0.0   0.0  175 days  /usr/lib/xorg/Xorg vt1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  |
|    0  8200     root     135MiB   0.1   0.4  117 days  python3 app.py xxxxxxxxx                                                                              |
|    0 19369     root     455MiB  62.4   2.5   20 days  python3 read_rtsp.py --path_stream xxxxxxxxxxxxxxxxxx                                                 |
|    0 30502     root     135MiB   0.0   1.8  16:33:59  python build_index.py                                                                                 |
|    1  1242     root       4MiB   0.0   0.0  175 days  /usr/lib/xorg/Xorg vt1 -displayfd 3 -auth xxxxxxx                                                     |
|    1 19422     root     455MiB  86.7   3.7   20 days  python3 read_rtsp.py --path_stream xxxxxxxxxxxxxxxxxxxxxxx                                            |
|    1 27877     root    2017MiB   9.4   2.2   15 days  python consumer.py                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      USER    TOTAL GPU MEM  TOTAL %CPU  TOTAL %MEM  |
+-----------------------------------------------------+
|      root          3210MiB       158.6        10.6  |
+-----------------------------------------------------+
```

## Reference
- [nvidia-htop](https://github.com/peci1/nvidia-htop/tree/master)
