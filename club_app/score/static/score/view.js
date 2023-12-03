
let chart_element = document.getElementById('chart');

window.onload = () => {
    console.log('start');
    select_exam();
    table_initialization();
    chart_initialization();
};

get_exam_label = () => {
    return new Promise(resolve => {
        $.get(`./exam_label`,(exam_label) => {
            resolve(exam_label);
        });
    });
};
get_exam_data = () => {
    return new Promise(resolve => {
        $.get(`./exam_data/${document.getElementById("exam-select").value}`,(exam_data) => {
            resolve(exam_data);
        });
    });
};
get_exam_chart = () => {
    return new Promise(resolve => {
        $.get(`./exam_chart/${document.getElementById("exam-select").value}`,(exam_chart) => {
            resolve(exam_chart);
        });
    });
};

async function table_initialization() {
    const exam_data = await get_exam_data();
    grid = new Grid({
        search: true,
        sort: true,
        columns: ['名前', '点数'],
        data: exam_data
    }).render(document.getElementById("score-table"));
}
async function update_table() {
    const exam_data = await get_exam_data();
    grid.updateConfig({
        search: true,
        sort: true,
        data: exam_data
    }).forceRender();
}

async function chart_initialization() {
    const chart_val = await get_exam_chart();
    new Chart(chart_element, {
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
async function update_chart() {
    const chart = await get_exam_chart();
    chart_label = chart[0]
    chart_data = chart[1]
}

async function select_exam() {
    const exam_label = await get_exam_label();
    
    //select要素を取得する
    for (let index = 0; index < exam_label.length; index++) {
        //option要素を新しく作る
        const option = document.createElement('option');
    
        //option要素にvalueと表示名を設定
        option.value = exam_label[index];
        option.textContent = exam_label[index];
    
        //select要素にoption要素を追加する
        document.getElementById("exam-select").appendChild(option);
    }
    document.getElementById("exam-select").onchange = event => {
        update_table();
    }
    
}

