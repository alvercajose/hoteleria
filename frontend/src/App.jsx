import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Clientes from "./pages/Clientes";
import Reservas from "./pages/Reservas";
import Habitaciones from "./pages/Habitaciones";
import Ingresos from "./pages/Ingresos";
import Egresos from "./pages/Egresos";
import Reportes from "./pages/Reportes";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/clientes" element={<Clientes />} />
        <Route path="/reservas" element={<Reservas />} />
        <Route path="/habitaciones" element={<Habitaciones />} />
        <Route path="/ingresos" element={<Ingresos />} />
        <Route path="/egresos" element={<Egresos />} />
        <Route path="/reportes" element={<Reportes />} />
      </Routes>
    </Router>
  );
}

export default App;
