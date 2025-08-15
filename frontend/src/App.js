import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Habitaciones from "./pages/Habitaciones";
import Clientes from "./pages/Clientes";
import Ingresos from "./pages/Ingresos";
import Egresos from "./pages/Egresos";
import Reportes from "./pages/Reportes";

function App(){
  return (
    <Router>
      <Navbar />
      <div style={{ padding: 16 }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/habitaciones" element={<Habitaciones />} />
          <Route path="/clientes" element={<Clientes />} />
          <Route path="/ingresos" element={<Ingresos />} />
          <Route path="/egresos" element={<Egresos />} />
          <Route path="/reportes" element={<Reportes />} />
        </Routes>
      </div>
    </Router>
    
  );
}

export default App;
