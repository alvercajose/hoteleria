import { useState, useEffect } from "react";
import "./Home.css"; // aquí pondremos los estilos de animación

export default function Home() {
  const imagenes = [
    "/habitacion.jpg",
    "/hotel-exterior.jpg"
   
  ];

  const [indice, setIndice] = useState(0);

  useEffect(() => {
    const intervalo = setInterval(() => {
      setIndice((prev) => (prev + 1) % imagenes.length);
    }, 5000);
    return () => clearInterval(intervalo);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="fondo-contenedor">
      <div
        className="fondo"
        style={{ backgroundImage: `url(${imagenes[indice]})` }}
      >
        <div className="overlay">
          <h1>Sistema Hotelería</h1>
          <p>Usa la navegación para ver Clientes, Habitaciones, Ingresos, Egresos y Reportes.</p>
        </div>
      </div>
    </div>
  );
}
