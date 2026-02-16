=============================

Referral Sharing Web App

Backend: aiohttp

Database: MongoDB (Motor async driver)

Frontend: Animated HTML + CSS + JS

=============================

from aiohttp import web import motor.motor_asyncio import os

MONGO_URI = "mongodb://localhost:27017" DB_NAME = "referral_db"

=============================

MongoDB Class

=============================

class ReferralDB: def init(self, uri=MONGO_URI, db_name=DB_NAME): self.client = motor.motor_asyncio.AsyncIOMotorClient(uri) self.db = self.client[db_name] self.collection = self.db["referrals"]

async def add_referral(self, data):
    return await self.collection.insert_one(data)

async def search_referrals(self, query=None, tag=None):
    filter_query = {}

    if query:
        filter_query["$or"] = [
            {"title": {"$regex": query, "$options": "i"}},
            {"description": {"$regex": query, "$options": "i"}},
            {"code": {"$regex": query, "$options": "i"}},
        ]

    if tag:
        filter_query["tags"] = tag

    return await self.collection.find(filter_query).to_list(100)

async def delete_referral(self, referral_id):
    from bson import ObjectId
    return await self.collection.delete_one({"_id": ObjectId(referral_id)})

routes = web.RouteTableDef() db = ReferralDB()

=============================

API Routes

=============================

@routes.get("/api/search") async def search_handler(request): query = request.query.get("q") tag = request.query.get("tag") results = await db.search_referrals(query, tag) for r in results: r["_id"] = str(r["_id"]) return web.json_response(results)

@routes.post("/api/add") async def add_handler(request): data = await request.json() await db.add_referral(data) return web.json_response({"status": "added"})

@routes.delete("/api/delete/{id}") async def delete_handler(request): await db.delete_referral(request.match_info["id"]) return web.json_response({"status": "deleted"})

=============================

Frontend UI

=============================

@routes.get("/") async def index(request): return web.Response(text=HTML_PAGE, content_type="text/html")

=============================

Animated HTML Interface

=============================

HTML_PAGE = """

<!DOCTYPE html><html>
<head>
<title>Referral Hub</title>
<style>
body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    color: white;
    overflow-x: hidden;
}header { text-align: center; padding: 20px; font-size: 28px; font-weight: bold; animation: fadeIn 1s ease-in-out; }

.search-bar { display: flex; justify-content: center; margin: 20px; }

.search-bar input { width: 300px; padding: 10px; border-radius: 30px; border: none; outline: none; transition: 0.3s; }

.search-bar input:focus { width: 400px; }

.tags { text-align: center; margin-bottom: 20px; }

.tag { display: inline-block; background: #ff9800; padding: 6px 12px; border-radius: 20px; margin: 5px; cursor: pointer; transition: 0.3s; }

.tag:hover { background: #ffc107; transform: scale(1.1); }

.card { background: rgba(255,255,255,0.1); margin: 10px auto; padding: 15px; border-radius: 15px; width: 80%; backdrop-filter: blur(10px); animation: slideUp 0.5s ease; }

button { background: #4caf50; border: none; padding: 8px 12px; border-radius: 8px; cursor: pointer; }

@keyframes fadeIn { from {opacity: 0} to {opacity: 1} }

@keyframes slideUp { from {transform: translateY(20px); opacity: 0} to {transform: translateY(0); opacity: 1} }

.admin-panel { position: fixed; right: 0; top: 0; background: rgba(0,0,0,0.8); padding: 20px; height: 100%; width: 250px; }

</style>
</head>
<body><header>🚀 Referral Code Hub</header><div class="search-bar">
    <input type="text" id="search" placeholder="Search by app, reward, code..." onkeyup="search()">
</div><div class="tags">
    <span class="tag" onclick="filterTag('high_reward')">🔥 High Reward</span>
    <span class="tag" onclick="filterTag('crypto')">💰 Crypto</span>
    <span class="tag" onclick="filterTag('shopping')">🛒 Shopping</span>
</div><div id="results"></div><div class="admin-panel">
    <h3>Admin Panel</h3>
    <input id="title" placeholder="Title"><br><br>
    <input id="code" placeholder="Code"><br><br>
    <input id="tags" placeholder="Tags (comma)"><br><br>
    <button onclick="addReferral()">Add</button>
</div><script>
async function search(tag=null) {
    const query = document.getElementById('search').value;
    let url = `/api/search?q=${query}`;
    if (tag) url += `&tag=${tag}`;
    const res = await fetch(url);
    const data = await res.json();
    display(data);
}

function filterTag(tag) {
    search(tag);
}

function display(data) {
    const container = document.getElementById('results');
    container.innerHTML = '';
    data.forEach(item => {
        container.innerHTML += `
            <div class="card">
                <h3>${item.title}</h3>
                <p>Code: <b>${item.code}</b></p>
                <p>Tags: ${item.tags}</p>
            </div>
        `;
    });
}

async function addReferral() {
    const title = document.getElementById('title').value;
    const code = document.getElementById('code').value;
    const tags = document.getElementById('tags').value.split(',');

    await fetch('/api/add', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({title, code, tags})
    });

    alert('Added!');
    search();
}

search();
</script></body>
</html>
"""=============================

App Init

=============================

async def web_server(): app = web.Application(client_max_size=30000000) app.add_routes(routes) return app
