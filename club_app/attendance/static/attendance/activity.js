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

    // 日付をクリックした時の処理
    $('td').on('click',() => {
        console.log('clicked');
        console.log($(this).text);
        if ($(this).text == '') return;
        if ($(this).hasClass('selected')){
            $(this).removeClass('selected');
        }else{
            $(this).addClass('selected');
        }
    });
};


async function render_calender(){

    $('#TableHead').text(`${YEAR}年${MONTH}月`);

    // td要素すべてを抽出
    const DAY_CELLS = document.evaluate('//td',document,null,XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,null);

    // monthのインデックスは0-11だから-1する
    let firstDay = new Date(`${YEAR}`,`${MONTH-1}`,1);
    let startDayWeek = firstDay.getDay();

    let lastDay = new Date(`${YEAR}`,`${MONTH}`,0);
    let lastDate = lastDay.getDate();


    // 出席記録のある日付を抽出
    const ACTIVITY_DAYS = await getActivityDays();

    let writeDay = 1;
    let arrayCheckIdx = 0;
    let hasActivity;

    // 月初めの曜日まで空白を埋める
    for (let i=0; i<startDayWeek; i++){
        cell = DAY_CELLS.snapshotItem(i);
        $(cell).text('');
        $(cell).removeClass('selected');
    };
    // 月最終日から月末まで空白を埋める
    for (let i=lastDate+1; i < DAY_CELLS.snapshotLength; i++){
        cell = DAY_CELLS.snapshotItem(i);
        $(cell).text('');
        $(cell).removeClass('selected');
    };

    // 日付を書き込む
    for (let i=startDayWeek; writeDay <= lastDate;i++){
        cell = DAY_CELLS.snapshotItem(i);
        // console.log(cell);
        $(cell).text(writeDay);
        $(cell).removeClass('selected');

        // 書き込もうとしている日付に出席していたか
        if (ACTIVITY_DAYS === 'None'){
            hasActivity = $(cell).hasClass('weekday');
        }else{
            [hasActivity,arrayCheckIdx] = checkInclude(writeDay,ACTIVITY_DAYS,arrayCheckIdx);
        }
        if (hasActivity){
            $(cell).addClass('selected')
        };
        writeDay++;
    };
};

getActivityDays = () => {
    return new Promise(resolve => {
        $.get(`./activity_data/${YEAR}/${MONTH}/`,(daysJson) => {
            days = JSON.parse(daysJson);
            resolve(days);
        });
    });
};

checkInclude = (day,array,idx) => {
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


