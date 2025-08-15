import { Link } from "react-router-dom";

export default function Navbar(){
  return (
    <nav>
      <div className="container">
        <Link to="/">Inicio</Link>
        <Link to="/habitaciones">Habitaciones</Link>
        <Link to="/clientes">Clientes</Link>
        <Link to="/ingresos">Ingresos</Link>
        <Link to="/egresos">Egresos</Link>
        <Link to="/reportes">Reportes</Link>
      </div>
    </nav>
  );
}
