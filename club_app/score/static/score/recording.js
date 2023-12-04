
get_exam_label = () => {
    return new Promise(resolve => {
        $.get(`./exam_label`,(exam_label) => {
            resolve(exam_label);
        });
    });
};

$('#exam-name').on('click focus', async function () {

	var options = await get_exam_label()
	
	$(this).autocomplete({
			source: options,
			minLength: 0,
			delay : 1,
			autoFocus: false,
			scroll:true,
	
	});
	
	$(this).autocomplete("search", "");
 
});