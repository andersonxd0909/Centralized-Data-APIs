import discord
from discord.ext import commands
from flask import Flask, jsonify
import threading
import random
import string
import secrets

# --- CONFIGURACIÓN ---
# He cambiado el token por un mensaje. Aquí debes poner tu nuevo token generado.
TOKEN = 'PON_AQUI_TU_TOKEN_DE_DISCORD' 

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
app = Flask(__name__)

# --- BASE DE DATOS DE LA API ---
# He anonimizado las IPs y los nombres de usuario.
db_seguridad = [
    {
        "id": 1, 
        "evento": "Login Exitoso", 
        "usuario": "USUARIO_GENERICO", 
        "ip": "0.0.0.0", 
        "nivel": "INFO"
    },
    {
        "id": 2, 
        "evento": "FUERZA BRUTA DETECTADA", 
        "usuario": "ADMIN_SISTEMA", 
        "ip": "0.0.0.0", 
        "nivel": "CRITICAL"
    }
]

# --- COMANDOS DEL BOT ---

@bot.command()
async def password(ctx, longitud: int = 16):
    """Genera una contraseña aleatoria usando la librería secrets"""
    alfabeto = string.ascii_letters + string.digits + string.punctuation
    # secrets es mejor que random para contraseñas porque es criptográficamente seguro
    password_segura = ''.join(secrets.choice(alfabeto) for i in range(longitud))
    await ctx.send(f"🔐 **Nueva Contraseña Segura:** `{password_segura}`")

@bot.command()
async def scan(ctx, ip: str = "127.0.0.1"):
    """Simula un escaneo de puertos"""
    puertos = [21, 22, 80, 443, 3306]
    await ctx.send(f"🔍 **Escaneando IP:** `{ip}`...")
    
    resultados = ""
    for p in puertos:
        estado = random.choice(["ABIERTO ✅", "CERRADO ❌"])
        resultados += f"Puerto {p}: {estado}\n"
    
    await ctx.send(f"📋 **Resultados:**\n{resultados}")

@bot.command()
async def alertas(ctx):
    """Muestra alertas de nivel CRITICAL de la lista db_seguridad"""
    criticos = [log for log in db_seguridad if log["nivel"] == "CRITICAL"]
    if not criticos:
        await ctx.send("✅ No hay alertas críticas actuales.")
    for alerta in criticos:
        await ctx.send(f"⚠️ **ALERTA**\nEvento: {alerta['evento']}\nIP: {alerta['ip']}")

# --- INICIO DE FLASK (API) Y BOT ---
@app.route('/api/v1/logs')
def get_logs(): 
    return jsonify(db_seguridad)

def run_flask(): 
    # Ejecuta el servidor web en el puerto 5000
    app.run(port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    # Usamos threading para que Flask y el Bot corran al mismo tiempo
    threading.Thread(target=run_flask).start()
    bot.run(TOKEN)