export default function Card({ title, children }) {
  return (
    <div className="card">
      <h4 style={{ marginTop: 0 }}>{title}</h4>
      {children}
    </div>
  );
}
