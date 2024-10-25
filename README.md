# DouyinLiveWebFetcher

DouyinLiveWebFetcher 是一个用于抓取抖音直播弹幕的工具。此项目使用 `pnpm` 和 Python 环境，下面是安装和配置的步骤。

## 环境安装与配置

### 1. 安装项目依赖

使用 `pnpm` 安装项目所需的依赖包：
   ```bash
   pnpm i
2. 创建 Python 虚拟环境并安装依赖
bash
复制代码
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
3. 启动 FastAPI 开发服务器
使用以下命令启动 FastAPI 服务器（若需本地运行，将 host 参数设置为 127.0.0.1）：

bash
复制代码
fastapi dev --host 0.0.0.0
服务器启动后，可以在浏览器中访问指定的地址。

修改直播间号
打开项目根目录中的 DouyinLiveWebFetcher-main\DouyinLiveWebFetcher-main\main.py 文件。

修改文件中的 live_id 值为目标直播间号，以抓取指定直播间的弹幕数据。

python
复制代码
from liveMan import DouyinLiveWebFetcher

if __name__ == '__main__':
    live_id = ''  # 在此输入直播间号
    DouyinLiveWebFetcher(live_id).start()
将 live_id 设置为目标直播间的编号后，保存文件即可。

访问地址
启动 FastAPI 服务器后，可以通过浏览器访问指定的地址进行互动和测试。

