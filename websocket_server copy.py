import asyncio
import websockets
from liveMan import DouyinLiveWebFetcher
from protobuf.douyin import ChatMessage
connected_clients = set()

async def handler(websocket, path):
    """处理前端WebSocket连接"""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Message from client: {message}")
    except websockets.ConnectionClosed:
        print("Connection closed")
    finally:
        connected_clients.remove(websocket)

async def broadcast(message):
    """向所有连接的客户端广播消息"""
    if connected_clients:
        await asyncio.wait([client.send(message) for client in connected_clients])

async def run_server():
    """运行WebSocket服务器"""
    server = await websockets.serve(handler, "localhost", 8765)
    await server.wait_closed()
def start_fetcher_and_broadcast(live_id):
    """启动DouyinLiveWebFetcher并通过WebSocket广播消息"""
    fetcher = DouyinLiveWebFetcher(live_id)

    # 修改 DouyinLiveWebFetcher 类中的 _parseChatMsg 方法，广播消息
    def new_parseChatMsg(payload):
        """聊天消息"""
        message = ChatMessage().parse(payload)
        user_name = message.user.nick_name
        content = message.content
        chat_message = f"【聊天msg】[{user_name}]: {content}"
        print(chat_message)

        # 广播弹幕消息给所有WebSocket客户端
        asyncio.run_coroutine_threadsafe(broadcast(chat_message), asyncio.get_event_loop())

    # 替换原有的 _parseChatMsg 方法
    fetcher._parseChatMsg = new_parseChatMsg

    # 启动抓取器
    fetcher.start()

async def main():
    """同时启动WebSocket服务器和抖音直播抓取"""
    # 启动WebSocket服务器
    server_task = asyncio.create_task(run_server())

    # 启动DouyinLiveWebFetcher抓取并广播弹幕（示例直播间ID）
    live_id = '6096197105'  # 替换为实际的直播间ID
    fetcher_task = asyncio.to_thread(start_fetcher_and_broadcast, live_id)

    await asyncio.gather(server_task, fetcher_task)


if __name__ == "__main__":
    asyncio.run(run_server())