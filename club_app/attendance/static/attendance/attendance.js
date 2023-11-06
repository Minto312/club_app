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
    const DAY_SELLS = document.evaluate('//td',document,null,XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,null);

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
    for (let i=start_day_week; write_day <= last_date;i++){
        cell = DAY_SELLS.snapshotItem(i);
        // console.log(cell);
        $(cell).text(write_day);

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
        $.get('./data/',(days_json) => {
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