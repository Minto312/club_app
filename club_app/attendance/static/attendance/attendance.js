const today = new Date();

let YEAR = today.getFullYear();
let MONTH = today.getMonth() + 1;
let DAY = 1;

window.onload = () => {
    console.log('start');

    $('#current-date').text(`${YEAR}-${MONTH}-${DAY}`);

    const DATE = `${YEAR}-${MONTH}-${DAY}`;
    $('#date').attr('value',DATE);

    render_calender();

    // 月を変更するボタン
    $('#next-month').on('click',() => {
        MONTH++;
        if (MONTH > 12){
            MONTH = 1;
            YEAR++;
        };
        render_calender();
    });
    $('#prev-month').on('click',() => {
        MONTH--;
        if (MONTH < 1){
            MONTH = 12;
            YEAR--;
        };
        render_calender();
    });
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


    // 出席記録のある日付を抽出
    const ATTENDED_DAYS = await get_attended_days();

    let write_day = 1;
    let array_check_idx = 0;
    let is_attended;

    // 月初めの曜日まで空白を埋める
    for (let i=0; i<start_day_week; i++){
        cell = DAY_CELLS.snapshotItem(i);
        $(cell).text('');
        $(cell).removeClass('attended');
    };
    // 月最終日から月末まで空白を埋める
    for (let i=last_date+1; i < DAY_CELLS.snapshotLength; i++){
        cell = DAY_CELLS.snapshotItem(i);
        $(cell).text('');
        $(cell).removeClass('attended');
    };

    // 日付を書き込む
    for (let i=start_day_week; write_day <= last_date;i++){
        cell = DAY_CELLS.snapshotItem(i);
        console.log(cell.class);
        $(cell).text(write_day);
        $(cell).removeClass('attended');

        // 書き込もうとしている日付に出席していたか
        [is_attended,array_check_idx] = check_include(write_day,ATTENDED_DAYS,array_check_idx);
        if (is_attended){
            $(cell).addClass('attended')
        };
        write_day++;
    };
};

get_attended_days = () => {
    return new Promise(resolve => {
        $.get(`./attendance_data/${YEAR}/${MONTH}/`,(days_json) => {
            days = JSON.parse(days_json);
            resolve(days);
        });
    });
};

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


