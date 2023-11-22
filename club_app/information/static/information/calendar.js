let today = new Date();

const YEAR = today.getFullYear();
const MONTH = today.getMonth() + 1;
const DAY = today.getDate();

window.onload = () => {
    console.log('start');

    $('#html_date').text(`${YEAR}年${MONTH}月${DAY}日`);

    const DATE = `${YEAR}-${MONTH}-${DAY}`;
    $('#date').attr('value',DATE);

    render_calender();
};

async function render_calender(){
    $('#TableHead').text(`${YEAR}年${MONTH}月`);

    // td要素すべてを抽出
    const DAY_CELLS = document.evaluate('//td',document,null,XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,null);

    // monthのインデックスは0-11だから-1する
    let first_day = new Date(`${YEAR}`,`${MONTH-1}`,1);
    let start_day_week = first_day.getDay();

    let last_day = new Date(`${YEAR}`,`${MONTH}`,0);
    let last_date = last_day.getDate();

    // カレンダーの各セルに日付を設定
    for (let i = 0; i < last_date; i++) {
        let cell = DAY_CELLS.snapshotItem(i + start_day_week);
        // day-${day}の形式のIDを生成
        const id = `day-${i+1}`;
        if (cell) {
            cell.id = id;
            cell.textContent = i + 1;
        }
    }

    const data = await get_attended_days();
    console.log(data);  // デバッグ: データをコンソールに出力
    for (let i = 0; i < data.length; i++) {
        const day = data[i][0];
        const has_club_activity = data[i][1];
        const element = document.getElementById(`day-${day}`);
        if (element) {
            if (has_club_activity) {
                element.classList.add('has-club-activity');  // 部活動がある日には特別なスタイルを適用
            }
        } else {
            console.error(`Element not found: day-${day}`);  // デバッグ: エラーメッセージをコンソールに出力
        }
    }
}

async function get_attended_days() {
    const response = await fetch('/information/data/');  // サーバーから日付データを取得
    const data = await response.json();  // レスポンスをJSON形式で解析
    console.log(data);  // デバッグ: レスポンスをコンソールに出力
    return data;  // 日付データを返す
}

check_include = (day,array,idx) => {
    let i = idx
    // 要素の最後まで確認できた時にはすべて使い終わっている
    // returnしたiがarrayのポインタになる
    if (i < array.length){
        if (day == array[i]){
            return [true,i];
        // arrayが昇順である前提
        }else if (day > array[i]){
            i++;
            return [false,i];
        };
    };
    return [false,i];
}