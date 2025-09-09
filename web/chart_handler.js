async function load() {
  const res = await fetch('./data/processed/dashboard.json');
  const data = await res.json();

  document.getElementById('total-in').textContent = fmt(data.totals.incoming);
  document.getElementById('total-out').textContent = fmt(data.totals.outgoing);
  document.getElementById('net').textContent = fmt(data.totals.net);

  const cat = data.by_category;
  new Chart(document.getElementById('byCategory'), {
    type: 'doughnut',
    data: {
      labels: cat.map(x => x.category),
      datasets: [{ data: cat.map(x => x.total) }]
    }
  });

  const months = data.monthly;
  new Chart(document.getElementById('monthly'), {
    type: 'line',
    data: {
      labels: months.map(x => x.month),
      datasets: [{ label: 'Total', data: months.map(x => x.total) }]
    },
    options: { tension: 0.25 }
  });

  const tbody = document.querySelector('#top-table tbody');
  data.top_counterparties.forEach(r => {
    const tr = document.createElement('tr');
    tr.innerHTML = `<td>${r.counterparty}</td><td>${r.count}</td><td>${fmt(r.total)}</td>`;
    tbody.appendChild(tr);
  });
}

function fmt(n) {
  return new Intl.NumberFormat('en-RW', { style: 'currency', currency: 'RWF', maximumFractionDigits: 0 }).format(n || 0);
}

load();
