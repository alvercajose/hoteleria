import { useEffect, useState } from "react";
import api from "../api/api";
import Loader from "../components/Loader";

export default function Egresos() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [form, setForm] = useState({ monto: "", fecha: "", concepto: "" });

  useEffect(() => fetchData(), []);

  function fetchData(){
    setLoading(true);
    api.get("/egresos")
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
    const payload = { ...form, monto: Number(form.monto) };
    api.post("/egresos", payload)
      .then(() => { setForm({ monto: "", fecha: "", concepto: "" }); fetchData(); })
      .catch(() => alert("Error al crear egreso"));
  }

  return (
    <div className="container">
      <h2>Egresos</h2>
      <form onSubmit={handleSubmit} style={{ maxWidth: 480 }}>
        <input name="monto" placeholder="Monto" value={form.monto} onChange={handleChange} />
        <input name="fecha" type="date" value={form.fecha} onChange={handleChange} />
        <input name="concepto" placeholder="Concepto" value={form.concepto} onChange={handleChange} />
        <button type="submit">Crear egreso</button>
      </form>

      {loading ? <Loader /> : (
        <div style={{ marginTop: 12 }}>
          {items.map(i => (
            <div className="card" key={i.id}>
              <p>{i.fecha} — {i.monto} — {i.concepto}</p>
            </div>
          ))}
          {items.length === 0 && <p>No hay egresos.</p>}
        </div>
      )}
    </div>
  );
}
