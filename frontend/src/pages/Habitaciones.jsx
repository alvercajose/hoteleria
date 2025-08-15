import { useEffect, useState } from "react";
import api from "../api/api";
import Loader from "../components/Loader";
import Card from "../components/Card";

export default function Habitaciones() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [form, setForm] = useState({ numero_habitacion: "", tipo_habitacion: "", precio: "", disponibilidad: true });

  useEffect(() => { fetchData(); }, []);

  function fetchData(){
    setLoading(true);
    api.get("/habitaciones")
      .then(r => setItems(r.data || []))
      .catch(err => { console.error(err); setItems([]); })
      .finally(() => setLoading(false));
  }

  function handleChange(e) {
    const { name, value, type, checked } = e.target;
    setForm(prev => ({ ...prev, [name]: type === "checkbox" ? checked : value }));
  }

  function handleSubmit(e) {
    e.preventDefault();
    // convertir precio a number si viene como string
    const payload = { ...form, precio: Number(form.precio) };
    api.post("/habitaciones", payload)
      .then(() => { setForm({ numero_habitacion: "", tipo_habitacion: "", precio: "", disponibilidad: true }); fetchData(); })
      .catch(err => alert("Error al crear habitación"));
  }

  return (
    <div className="container">
      <h2>Habitaciones</h2>
      <form onSubmit={handleSubmit} style={{ maxWidth: 480 }}>
        <input name="numero_habitacion" placeholder="Número" value={form.numero_habitacion} onChange={handleChange} />
        <input name="tipo_habitacion" placeholder="Tipo" value={form.tipo_habitacion} onChange={handleChange} />
        <input name="precio" placeholder="Precio" value={form.precio} onChange={handleChange} />
        <label><input type="checkbox" name="disponibilidad" checked={form.disponibilidad} onChange={handleChange} /> Disponible</label>
        <button type="submit">Crear habitación</button>
      </form>

      {loading ? <Loader /> : (
        <div style={{ display: "flex", flexWrap: "wrap", marginTop: 12 }}>
          {items.map(h => (
            <Card key={h.id} title={h.numero_habitacion || `ID ${h.id}`}>
              <p>Tipo: {h.tipo_habitacion}</p>
              <p>Precio: {h.precio}</p>
              <p>Disponible: {h.disponibilidad ? "Sí" : "No"}</p>
            </Card>
          ))}
          {items.length === 0 && <p>No hay habitaciones.</p>}
        </div>
      )}
    </div>
  );
}
