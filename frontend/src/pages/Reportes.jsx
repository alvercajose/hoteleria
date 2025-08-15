import { useEffect, useState } from "react";
import api from "../api/api";
import Loader from "../components/Loader";

export default function Reportes() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [form, setForm] = useState({ tipo_reporte: "", fecha: "", contenido: "" });

  useEffect(() => fetchData(), []);

  function fetchData(){
    setLoading(true);
    api.get("/reportes")
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
    api.post("/reportes", form)
      .then(() => { setForm({ tipo_reporte: "", fecha: "", contenido: "" }); fetchData(); })
      .catch(() => alert("Error al crear reporte"));
  }

  return (
    <div className="container">
      <h2>Reportes</h2>
      <form onSubmit={handleSubmit} style={{ maxWidth: 480 }}>
        <input name="tipo_reporte" placeholder="Tipo de reporte" value={form.tipo_reporte} onChange={handleChange} />
        <input name="fecha" type="date" value={form.fecha} onChange={handleChange} />
        <textarea name="contenido" placeholder="Contenido" value={form.contenido} onChange={handleChange} style={{ width: "100%", minHeight: 100 }} />
        <button type="submit">Crear reporte</button>
      </form>

      {loading ? <Loader /> : (
        <div style={{ marginTop: 12 }}>
          {items.map(r => (
            <div className="card" key={r.id}>
              <p><strong>{r.tipo_reporte}</strong> — {r.fecha}</p>
              <p>{r.contenido}</p>
            </div>
          ))}
          {items.length === 0 && <p>No hay reportes.</p>}
        </div>
      )}
    </div>
  );
}
