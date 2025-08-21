document.addEventListener('DOMContentLoaded', () => {
  const form    = document.getElementById('prefsForm');
  const results = document.getElementById('results');

  form.addEventListener('submit', async e => {
    e.preventDefault();
    results.innerHTML = ''; 

    const prefs = {
      budget:        parseFloat(document.getElementById('budget').value),
      meals_per_day: parseInt(document.getElementById('meals').value, 10),
      max_time:      parseInt(document.getElementById('maxTime').value, 10),
      diet:          document.getElementById('diet').value,
      skill:         document.getElementById('skill').value,
      cuisine:       document.getElementById('cuisine').value.trim().toLowerCase(),
      allergies:     document.getElementById('allergies').value
                        .split(',')
                        .map(a => a.trim().toLowerCase())
                        .filter(a => a)
    };

    try {
      const res = await fetch('/api/mealplan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(prefs)
      });

      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.error || 'Unknown server error');
      }

      const data = await res.json();

      let totalCost = 0;

      // Meal Plan Rows with Cost Column
      const mealRows = data.meals.map((m, i) => {
        const day  = Math.floor(i / prefs.meals_per_day) + 1;
        const slot = (i % prefs.meals_per_day) + 1;
        const cost = m.cost ?? 0; // fallback if cost is missing
        totalCost += cost;

        return `
          <tr>
            <th scope="row">Day ${day}</th>
            <td>Meal ${slot}</td>
            <td>${m.name}</td>
            <td>${m.prep_time} mins</td>
            <td>£${cost.toFixed(2)}</td>
          </tr>`;
      }).join('');

      const groceryRows = Object.entries(data.grocery).map(
        ([item, qty]) => `
          <tr>
            <td>${item}</td>
            <td>${qty}</td>
          </tr>`).join('');

      results.innerHTML = `
        <div class="card mb-4">
          <div class="card-header d-flex justify-content-between align-items-center">
            <span>Weekly Meal Plan</span>
            <span class="text-success fw-bold">Estimated Total Cost: £${totalCost.toFixed(2)}</span>
          </div>
          <div class="table-responsive">
            <table class="table table-dark table-striped text-center mb-0">
              <thead>
                <tr>
                  <th>Day</th><th>Meal</th><th>Recipe</th><th>Prep Time</th><th>Cost</th>
                </tr>
              </thead>
              <tbody>${mealRows}</tbody>
            </table>
          </div>
        </div>

        <div class="card">
          <div class="card-header">Grocery List</div>
          <div class="table-responsive">
            <table class="table table-dark table-striped text-center mb-0">
              <thead>
                <tr><th>Item</th><th>Quantity</th></tr>
              </thead>
              <tbody>${groceryRows}</tbody>
            </table>
          </div>
        </div>`;
    } catch (err) {
      results.innerHTML = `
        <div class="alert alert-danger text-center" role="alert">
          ${err.message}
        </div>`;
    }
  });
});
