a
    ja�`�  �                   @   s\  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	zd dl
Z
W n( ey|   ed� ed� e�  Y n0 dd� Zdd� Zdd	� Ze�  e�  ed
� q�q�d Zzejd dkr�dZW n ey�   d ZY n0 edk�red� e�  e�  �nVed k�rXed� ed�Zdev �rJee�Ze�d� d�e�Ze�� Zee�dk�sfee�dk �rred� �qede d �Zee�dk�r�ed� �qee Ze�� �s�ed� �qde Zed�Z e
�!dee dd��Z"ee"�#� � ed� �qXde"j v �red� ed � e�  e�  d!e"j v �rNed"� ed#� ed � e�  e�  e�  �qdS )$�    Nz.Error !! : Some dependencies are not installedzIError to import 'requests' Library
todo : python3 -m pip install requestsc                   C   s$   t jdkrt �d� n
t �d� d S )N�nt�cls�clear)�os�name�system� r   r   �Tools/fakesms.py�clr   s    
r
   c                  C   s   t �  d} t| � td� d S )Na;                                                    
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[  ___  __      ___   _      ___   _      ___   _      ___   _  ]
[ [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=| ]
[  '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_| ]
[  /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  / ]
[       |____________|____________|____________|____________|   ]
[                             |            |            |       ]
[                         ___  \_      ___  \_      ___  \_     ]
[                        [(_)] |=|    [(_)] |=|    [(_)] |=|    ]
[                         '-`  |_|     '-`  |_|     '-`  |_|    ]
[                        /mmm/        /mmm/        /mmm/        ]
[                                                               ]
version = V2       
<Facebook> =  [ [1;31mMichael Meled ]
<Name> =      [ [1;31mMichael       ]
<Nick Name> = [ [1;31mHacker        ]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
                                         �
)r
   �print)Zlogor   r   r	   �banner   s    r   c                  C   sB   t d�} t�d| � �� t d� td� td� td� t�  d S )NzEnter Text ID of X-SMS 
	 -->>z!curl https://textbelt.com/status/z
Press Enter To Exit..z
Thanks For Using X-SMS..z;	We Hope To See You Again
 Type bash Run.sh
	To Run Again..�Thank you for Your Time...)�inputr   r   r   �exit)ZTXTIDr   r   r	   �Track3   s    r   z0[0mThis Tool Is Used To Send Anonymous Messages�   Ztrackz5Track The Anonymous Message You Sent Using This Tool.zBEnter The Details Of The Person You Want To Send Anonymous Messagez"	Enter Country Code (Without +) : �+� �   zE

Invalid Country Code..
		Country Codes Are Generally 1-3 digits...
zEnter Phone Number : +� �   z

Invalid Phone Number..
z,

Phone Number Must Consist Of Numbers Only
zEnter Message to send : zhttps://textbelt.com/textZtextbelt)Zphone�message�keyr   z"success" : true z#[92m Message Sent Succesfully [0mz
		Press Enter To Exit...z"success" : false z[91m Error Occuredz[91m Failed to send SMS! )$Z	threading�string�base64Zurllib.requestZurllib�urllib.parser   �time�sysZrandomZrequests�ImportErrorr   r   r
   r   r   �type�argv�	Exceptionr   Zcc�listZtc�remove�join�strip�lenZpnZnumbe�isdigitZreceiver�textZpostZrespZjsonr   r   r   r	   �<module>   s�   	







�