import os

html = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Mensaje de Amor</title>
<style>
body {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    font-family: Arial, sans-serif;
    text-align: center;
}

.contenedor {
    color: white;
    z-index: 2;
}

.mensaje {
    font-size: 40px;
    animation: latido 1.5s infinite;
}

.nombre {
    font-size: 22px;
    margin-top: 10px;
}

@keyframes latido {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}

.corazon {
    position: absolute;
    bottom: -20px;
    font-size: 24px;
    animation: flotar 6s linear infinite;
}

@keyframes flotar {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(-110vh); opacity: 0; }
}
</style>
</head>
<body>

<div class="contenedor">
    <div class="mensaje">💖 Te amo amo mucho 💖</div>
    <div class="nombre">Para: Juan Carlos de Jesús Fernández</div>
</div>

<script>
function crearCorazon() {
    const corazon = document.createElement("div");
    corazon.className = "corazon";
    corazon.innerHTML = "❤️";
    corazon.style.left = Math.random() * 100 + "vw";
    corazon.style.animationDuration = (Math.random() * 3 + 4) + "s";
    document.body.appendChild(corazon);
    setTimeout(() => corazon.remove(), 7000);
}
setInterval(crearCorazon, 300);
</script>

</body>
</html>
"""

# Crear archivo HTML
nombre_archivo = "mensaje_amor.html"
with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write(html)

# Generar link universal
ruta = os.path.abspath(nombre_archivo)
link = f"file:///{ruta.replace(os.sep, '/')}"

print("💌 COPIA ESTE LINK Y ÁBRELO EN CUALQUIER NAVEGADOR 💌\n")
print(link)
