# linebot_practice

�o�O�@�Өϥ� Python �P Flask ��@�� LINE Bot �d�ұM�סA�]�t�^�Ф�r�B�Ϥ��B�a�I�T���A�þ�X�F��H�B�a�_��T�d�ߡA�H�ιϤ��W�Ǩ� Google Drive �M�l��H�e�\��C

---

## �\��S��

- ��r�T������r�^�С]�p���۩I�B�D�U���^
- �^�ǹϤ��P�a�I�T��
- �d�߮�H�ϡ]�Y�ɤѮ�Ϥ��^
- �a�_��T�d�߻P�Ϥ��^�ǡ]�ϥΥx�W������H���}���ơ^
- �U���Τ�ǰe���Ϥ��äW�Ǩ� Google Drive
- �N���쪺�Ϥ��μv���H Email �H�e����w�H�c
- �^�ǨϥΪ̶ǰe���K��
- �ϥ� Flask �@�� Webhook Server�A���� LINE �T���ƥ�

---

## ���һݨD

- Python 3.8+
- Flask 3.0.3
- line-bot-sdk 3.13.0
- protobuf 5.28.2
- google-api-python-client 2.149.0
- ��L�̿�M��]requests�Bgoogle-auth ���^

---

## �w�ˤ覡

1. ��ĳ�ϥε������ҡG
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

2. �w�˩Ҧ��M��:
pip install -r requirements.txt

## �M�׵��c

linebot_practice/
�x
�u�w�w main.py                 # Flask ���A���P LINE Bot Webhook �J�f
�u�w�w Email.py                # �H�e�l��\��Ҳ�
�u�w�w earthquake.py           # �a�_��T�����P�B�z�Ҳ�
�u�w�w drive_image.py          # �Ϥ��W�Ǧ� Google Drive �\��Ҳ�
�u�w�w database.py             # ��Ʈw�����\��]�������Φۦ��X�R�^
�u�w�w requirements.txt        # Python �M��M��
�|�w�w README.md               # �M�׻������
