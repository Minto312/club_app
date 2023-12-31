let chart_element = document.getElementById('chart');

window.onload = async () => {
    console.log('start');
    await select_exam();
    await chart_initialization();
    await table_initialization();
    document.getElementById("exam-select").onchange = async () => {
        await update_chart();
        await update_table();
    }
};

get_exam_label = () => {
    return new Promise(resolve => {
        $.get(`./exam_label`,(exam_label) => {
            resolve(exam_label);
        });
    });
};
get_exam_data = () => {
    const exam_name = document.getElementById("exam-select").value;
    return new Promise(resolve => {
        $.get(`./exam_data/${exam_name}`,(exam_data) => {
            resolve(exam_data);
        });
    });
};
get_exam_chart = () => {
    return new Promise(resolve => {
        const exam_name = document.getElementById("exam-select").value;
        $.get(`./exam_chart/${exam_name}`,(exam_chart) => {
            resolve(exam_chart);
        });
    });
};

async function table_initialization() {
    const exam_data = await get_exam_data();
    grid = new gridjs.Grid({
        height: '100%',
        width: '100%',
        search: true,
        sort: true,
        pagination: {
            limit: 7
        },
        columns: ['名前', '点数'],
        data: exam_data
    }).render(document.getElementById("score-table"));
}
async function update_table() {
    const exam_data = await get_exam_data();
    grid.updateConfig({
        data: exam_data
    }).forceRender();
}

async function chart_initialization() {
    const chart_val = await get_exam_chart();
    chart = new Chart(chart_element, {
        responsive: true,
        maintainAspectRatio: false,
        type: 'bar',
        data: {
            labels: chart_val[0],
            datasets: [{
                label: '',
                data: chart_val[1],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    chart.canvas.parentNode.style.height = '50vh';
    chart.canvas.parentNode.style.width = '90%';
}
async function update_chart() {
    chart.destroy();
    const chart_val = await get_exam_chart();
    chart = new Chart(chart_element, {
        type: 'bar',
        data: {
            labels: chart_val[0],
            datasets: [{
                label: '',
                data: chart_val[1],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

async function select_exam() {
    const exam_label = await get_exam_label();
    for (let index = 0; index < exam_label.length; index++) {
        const option = document.createElement('option');
        option.value = exam_label[index];
        option.textContent = exam_label[index];
        document.getElementById("exam-select").appendChild(option);
    }
}