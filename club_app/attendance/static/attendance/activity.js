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
    $('td').on('click',function(){
        console.log('clicked');
        console.log($(this).text);
        console.log($(this));
        if ($(this).text == '') return;
        if ($(this).hasClass('selected')){
            $(this).removeClass('selected');
        }else{
            $(this).addClass('selected');
        }
    });

    // 送信ボタンを押した時の処理
    $('button#submit').on('click',() => {
        console.log('submit');
        csrfSetting();
        postSelectedDays();
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
            hasActivity = ACTIVITY_DAYS[writeDay] !== undefined;
        }
        if (hasActivity){
            $(cell).addClass('selected')
        };
        writeDay++;
    };
};

const getActivityDays = () => {
    return new Promise(resolve => {
        $.get(`./activity_data/${YEAR}/${MONTH}/`,(days) => {
            if (days === 'None'){
                resolve(days);
            }else{
                resolve(JSON.parse(days));
            }
        });
    });
};

// ref: https://sleepless-se.net/2019/12/07/post-with-csrftoken/#google_vignette
// 2 csrfを取得、設定する関数
function getCookie(key) {
    var cookies = document.cookie.split(';');
    for (var _i = 0, cookies_1 = cookies; _i < cookies_1.length; _i++) {
        var cookie = cookies_1[_i];
        var cookiesArray = cookie.split('=');
        if (cookiesArray[0].trim() == key.trim()) {
            return cookiesArray[1]; // (key[0],value[1])
        }
    }
    return '';
}
function csrfSetting() {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
}

// 3 POST以外は受け付けないようにする関数
function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
const postSelectedDays = () => {
    console.log('post');
    const selectedDays = $('.selected');
    let selectedDaysObj = {};
    for (let i=0; i<selectedDays.length; i++){
        selectedDaysObj[selectedDays[i].textContent] = 'true';
    };
    console.log(selectedDaysObj)
    const selectedDaysJson = JSON.stringify(selectedDaysObj);
    console.log(selectedDaysJson);
    console.log(`./register/${YEAR}/${MONTH}/`);
    $.post(`./register/${YEAR}/${MONTH}/`,{'days':selectedDaysJson},(res) => {
        console.log(res);
        alert('登録しました');
    });
}