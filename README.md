pnpm i
python -m venv venv
pip install -r requirements.txt
fastapi dev --host 0.0.0.0(Adjust the parameters to 127.0.0.1 to run locally)
Just access the address using your browser


You can do it in DouyinLiveWebFetcher-main\DouyinLiveWebFetcher-main\main.py
Modify the live broadcast room number inside


from liveMan import DouyinLiveWebFetcher

if __name__ == '__main__':
    live_id = ''
    DouyinLiveWebFetcher(live_id).start()

you can take the live_id in this
