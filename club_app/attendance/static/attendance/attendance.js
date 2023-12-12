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

    $('#absent-button').on('click',() => {
        $.get(`./attend/False`,(res) => {
            alert('欠席にしました');
            console.log(res);
        });
    });

    $('#attend-code').on('click',() => {
        const codeUrl = 'https://' + location.hostname + location.pathname + 'attend/True';
        $('#code').qrcode(codeUrl);
        $('#code-container').show();
        $('#close').on('click',() => {
            $('#code-container').hide();
            $('#code').clear();
        })
    })
};


const render_calender = async () => {

    $('#TableHead').text(`${YEAR}年${MONTH}月`);

    // td要素すべてを抽出
    const DAY_CELLS = document.evaluate('//td',document,null,XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,null);

    // monthのインデックスは0-11だから-1する
    let first_day = new Date(`${YEAR}`,`${MONTH-1}`,1);
    let start_day_week = first_day.getDay();

    let last_day = new Date(`${YEAR}`,`${MONTH}`,0);
    let last_date = last_day.getDate();


    // 出席記録のある日付を抽出
    const ATTENDED_DAYS = await getAttendedDays();
    const ACTIVITY_DAYS = await getActivityDays();

    let write_day = 1;

    // 月初めの曜日まで空白を埋める
    for (let i=0; i<start_day_week; i++){
        cell = DAY_CELLS.snapshotItem(i);
        $(cell).text('');
        $(cell).removeClass('attended');
        $(cell).removeClass('absent');
        $(cell).removeClass('activity');
    };
    // 月最終日から月末まで空白を埋める
    for (let i=last_date+1; i < DAY_CELLS.snapshotLength; i++){
        cell = DAY_CELLS.snapshotItem(i);
        $(cell).text('');
        $(cell).removeClass('attended');
        $(cell).removeClass('absent');
        $(cell).removeClass('activity');
    };

    // 日付を書き込む
    for (let i=start_day_week; write_day <= last_date;i++){
        cell = DAY_CELLS.snapshotItem(i);
        $(cell).text(write_day);
        $(cell).removeClass('attended');
        $(cell).removeClass('absent');
        $(cell).removeClass('activity');

        // 書き込もうとしている日付に出席していたか
        if (ATTENDED_DAYS[write_day] !== undefined){

            if (ATTENDED_DAYS[write_day] == 'attend'){
                $(cell).addClass('attended');
            }else if (ATTENDED_DAYS[write_day] == 'absent'){
                $(cell).addClass('absent');
            }
        }
        // 書き込もうとしている日付に活動があるか
        if (ACTIVITY_DAYS !== 'None'){
            if (ACTIVITY_DAYS[write_day] !== undefined){
                $(cell).addClass('activity');
            }
        }
        write_day++;
    };
};

const getAttendedDays = () => {
    return new Promise(resolve => {
        $.get(`./attendance_data/${YEAR}/${MONTH}/`,(days_json) => {
            days = JSON.parse(days_json);
            console.log(`days: ${days}`);
            resolve(days);
        });
    });
};
const getActivityDays = () => {
    return new Promise(resolve => {
        $.get(`./activity/activity_data/${YEAR}/${MONTH}/`,(days) => {
            if (days === 'None'){
                resolve(days);
            }else{
                resolve(JSON.parse(days));
            }
        });
    });
};
