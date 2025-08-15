import { useEffect, useState } from "react";
import api from "../api/api";
import Loader from "../components/Loader";
import Card from "../components/Card";

export default function Clientes() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [form, setForm] = useState({ nombre: "", telefono: "", correo: "", direccion: "" });

  useEffect(() => fetchData(), []);

  function fetchData(){
    setLoading(true);
    api.get("/clientes")
      .then(r => setItems(r.data || []))
      .catch(err => { console.error(err); setItems([]); })
      .finally(() => setLoading(false));
  }

  function handleChange(e) {
    const { name, value } = e.target;
    setForm(prev => ({ ...prev, [name]: value }));
  }

  function handleSubmit(e) {
    e.preventDefault();
    api.post("/clientes", form)
      .then(() => { setForm({ nombre: "", telefono: "", correo: "", direccion: "" }); fetchData(); })
      .catch(err => alert("Error al crear cliente"));
  }

  return (
    <div className="container">
      <h2>Clientes</h2>
      <form onSubmit={handleSubmit} style={{ maxWidth: 480 }}>
        <input name="nombre" placeholder="Nombre" value={form.nombre} onChange={handleChange} />
        <input name="telefono" placeholder="Teléfono" value={form.telefono} onChange={handleChange} />
        <input name="correo" placeholder="Correo" value={form.correo} onChange={handleChange} />
        <input name="direccion" placeholder="Dirección" value={form.direccion} onChange={handleChange} />
        <button type="submit">Crear cliente</button>
      </form>

      {loading ? <Loader /> : (
        <div style={{ marginTop: 12 }}>
          {items.map(c => (
            <Card key={c.id} title={c.nombre}>
              <p>Tel: {c.telefono}</p>
              <p>Email: {c.correo}</p>
              <p>{c.direccion}</p>
            </Card>
          ))}
          {items.length === 0 && <p>No hay clientes.</p>}
        </div>
      )}
    </div>
  );
}
