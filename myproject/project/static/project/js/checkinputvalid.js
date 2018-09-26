
function checkIsovalid()
{
	
	if(sessionStorage.getItem("loginSuccess") != "true"){
	  
		alert("Please login.")
		return;
	}else{
		//alert("ok");
		var age = document.getElementsByName("Age");
		var grip = document.getElementsByName("grip");
		var plantarflexors = document.getElementsByName("Plantarflexors");
		var Dorsiflexors = document.getElementsByName("Dorsiflexors");
		var Knee_flexors = document.getElementsByName("Knee flexors");
		var Knee_extension = document.getElementsByName("Knee extension");
		var Hip_abductors = document.getElementsByName("Hip abductors");
		var Hip_external_rotators = document.getElementsByName("Hip external rotators");
		var Hip_internal_rotators = document.getElementsByName("Hip internal rotators");
		var Elbow_flexors = document.getElementsByName("Elbow flexors");
		var Elbow_extensors = document.getElementsByName("Elbow extensors");
		var Shoulder_external_rotators = document.getElementsByName("Shoulder external rotators");
		var Shoulder_internal_rotators = document.getElementsByName("Shoulder internal rotators");
		if(age[0].value ==""||isNaN(age[0].value) || age[0].value <= 0 || (age[0].value)%1!==0)
		{
		alert("Input Age Not Valid");
		}else if(grip[0].value ==""||isNaN(grip[0].value) || grip[0].value <= 0){
			alert("Input Grip Not Valid");
		}else if(plantarflexors[0].value ==""||isNaN(plantarflexors[0].value) || plantarflexors[0].value < 0){
			alert("Input plantarflexors Not Valid");
		}else if(Dorsiflexors[0].value ==""||isNaN(Dorsiflexors[0].value) || Dorsiflexors[0].value < 0){
			alert("Input Dorsiflexors Not Valid");
		}else if(Knee_flexors[0].value ==""||isNaN(Knee_flexors[0].value) || Knee_flexors[0].value <= 0){
			alert("Input Knee flexors Not Valid");
		}else if(Knee_extension[0].value ==""||isNaN(Knee_extension[0].value) || Knee_extension[0].value <= 0){
			alert("Input Knee extension Not Valid");
		}else if(Hip_abductors[0].value ==""||isNaN(Hip_abductors[0].value) || Hip_abductors[0].value <= 0){
			alert("Input Hip abductors Not Valid");
		}else if(Hip_external_rotators[0].value ==""||isNaN(Hip_external_rotators[0].value) || Hip_external_rotators[0].value <= 0){
			alert("Input Hip external rotators Not Valid");
		}else if(Hip_internal_rotators[0].value ==""||isNaN(Hip_internal_rotators[0].value) || Hip_internal_rotators[0].value <= 0){
			alert("Input Hip internal rotators Not Valid");
		}else if(Elbow_flexors[0].value ==""||isNaN(Elbow_flexors[0].value) || Elbow_flexors[0].value <= 0){
			alert("Input Elbow flexors Not Valid");
		}else if(Elbow_extensors[0].value ==""||isNaN(Elbow_extensors[0].value) || Elbow_extensors[0].value <= 0){
			alert("Input Elbow extensors Not Valid");
		}else if(Shoulder_external_rotators [0].value ==""||isNaN(Shoulder_external_rotators [0].value) || Shoulder_external_rotators [0].value <= 0){
			alert("Input Shoulder external rotators Not Valid");
		}else if(Shoulder_internal_rotators[0].value ==""||isNaN(Shoulder_internal_rotators[0].value) || Shoulder_internal_rotators[0].value <= 0){
			alert("Input Shoulder internal rotators Not Valid");
		}else {
			data_send = {'age':age[0].value,
				'gender':document.getElementsByName("gender")[0].value,
				'gs':grip[0].value,
				'apfs':plantarflexors[0].value,
				'ads':Dorsiflexors[0].value,
				'kfs':Knee_flexors[0].value,
				'kes':Knee_extension[0].value,
				'has':Hip_abductors[0].value,
				'hers':Hip_external_rotators[0].value,
				'hirs':Hip_internal_rotators[0].value,
				'efs':Elbow_flexors[0].value,
				'ees':Elbow_extensors[0].value,
				'sers':Shoulder_external_rotators [0].value,
				'sirs':Shoulder_internal_rotators[0].value,
			};
			$.ajax({
		        url:"/ims/submit", //提交到那里
		        type:"POST", //提交类型
		        data:JSON.stringify(data_send), //提交的数据
		        success:function(data){ //success不会直接运行，当服务器有数据传输过来才会触发执行。
		　　　　	console.log('responsed data:');
		        //console.log(data);
		        cm = data['compare_model'];
		        raw = data['user_raw_data'];
		        console.log(raw);
		        console.log(cm);
		        $("#gs").text("Standard value: "+ cm['gs_mean'] + ", Evaluation: " + raw['gs_eval']);
		        $("#apfs").text("Standard value: "+ cm['apfs_mean'] + ", Evaluation: " + raw['apfs_eval']);
		        $("#ads").text("Standard value: "+ cm['ads_mean'] + ", Evaluation: " + raw['ads_eval']);
		        $("#kfs").text("Standard value: "+ cm['kfs_mean'] + ", Evaluation: " + raw['kfs_eval']);
		        $("#kes").text("Standard value: "+ cm['kes_mean'] + ", Evaluation: " + raw['kes_eval']);
		        $("#has").text("Standard value: "+ cm['has_mean'] + ", Evaluation: " + raw['has_eval']);
		        $("#hers").text("Standard value: "+ cm['hers_mean'] + ", Evaluation: " + raw['hers_eval']);
		        $("#hirs").text("Standard value: "+ cm['hirs_mean'] + ", Evaluation: " + raw['hirs_eval']);
		        $("#efs").text("Standard value: "+ cm['efs_mean'] + ", Evaluation: " + raw['efs_eval']);
		        $("#ees").text("Standard value: "+ cm['ees_mean'] + ", Evaluation: " + raw['ees_eval']);
		        $("#sers").text("Standard value: "+ cm['sers_mean'] + ", Evaluation: " + raw['sers_eval']);
		        $("#sirs").text("Standard value: "+ cm['sirs_mean'] + ", Evaluation: " + raw['sirs_eval']);
		        
				var x = document.getElementById("iso_result");
				x.style.display = (x.style.display == 'none')?'block':'none';

		    	}
		    })	
		}
	}

}


function checkMotionvalid()
{
	if(sessionStorage.getItem("loginSuccess") != "true"){
	  
		alert("Please login.")
		return;
	}else{
		//alert("ok");
		var age = document.getElementsByName("Age");
		var Neck_flexion= document.getElementsByName("Neck flexion");
		var Neck_extension= document.getElementsByName("Neck extension");
		var plantarflexion = document.getElementsByName("Plantarflexion");
		var Dorsiflexion = document.getElementsByName("Dorsiflexion");
		var Knee_flexion = document.getElementsByName("Knee flexion");
		var Knee_extension = document.getElementsByName("Knee extension");
		var Hip_flexion = document.getElementsByName("Hip flexion");
		var Hip_external_rotators = document.getElementsByName("Hip external rotators");
		var Hip_internal_rotators = document.getElementsByName("Hip internal rotators");
		var Elbow_flexion = document.getElementsByName("Elbow flexion");
		var Elbow_extension = document.getElementsByName("Elbow extension");
		var Shoulder_external_rotation = document.getElementsByName("Shoulder external rotation");
		var Shoulder_internal_rotation = document.getElementsByName("Shoulder internal rotation");
		if(age[0].value ==""||isNaN(age[0].value) || age[0].value <= 0 || (age[0].value)%1!==0)
		{
		alert("Input Age Not Valid");
		}else if(Neck_flexion[0].value ==""||isNaN(Neck_flexion[0].value) || Neck_flexion[0].value <= 0){
			alert("Input Neck flexion Not Valid");
		}else if(Neck_extension[0].value ==""||isNaN(Neck_extension[0].value) || Neck_extension[0].value <= 0){
			alert("Input Neck extension Not Valid");
		}else if(plantarflexion[0].value ==""||isNaN(plantarflexion[0].value) || plantarflexion[0].value < 0){
			alert("Input plantarflexion Not Valid");
		}else if(Dorsiflexion[0].value ==""||isNaN(Dorsiflexion[0].value) || Dorsiflexion[0].value < 0){
			alert("Input Dorsiflexion Not Valid");
		}else if(Knee_flexion[0].value ==""||isNaN(Knee_flexion[0].value) || Knee_flexion[0].value <= 0){
			alert("Input Knee flexion Not Valid");
		}else if(Knee_extension[0].value ==""||isNaN(Knee_extension[0].value) || Knee_extension[0].value <= 0){
			alert("Input Knee extension Not Valid");
		}else if(Hip_flexion[0].value ==""||isNaN(Hip_flexion[0].value) || Hip_flexion[0].value <= 0){
			alert("Input Hip flexion Not Valid");
		}else if(Hip_external_rotators[0].value ==""||isNaN(Hip_external_rotators[0].value) || Hip_external_rotators[0].value <= 0){
			alert("Input Hip external rotators Not Valid");
		}else if(Hip_internal_rotators[0].value ==""||isNaN(Hip_internal_rotators[0].value) || Hip_internal_rotators[0].value <= 0){
			alert("Input Hip internal rotators Not Valid");
		}else if(Elbow_flexion[0].value ==""||isNaN(Elbow_flexion[0].value) || Elbow_flexion[0].value <= 0){
			alert("Input Elbow flexion Not Valid");
		}else if(Elbow_extension[0].value ==""||isNaN(Elbow_extension[0].value) || Elbow_extension[0].value <= 0){
			alert("Input Elbow extension Not Valid");
		}else if(Shoulder_external_rotation [0].value ==""||isNaN(Shoulder_external_rotation [0].value) || Shoulder_external_rotation [0].value <= 0){
			alert("Input Shoulder external rotation Not Valid");
		}else if(Shoulder_internal_rotation[0].value ==""||isNaN(Shoulder_internal_rotation[0].value) || Shoulder_internal_rotation[0].value <= 0){
			alert("Input Shoulder internal rotation Not Valid");
		}else {

			data_send = {
				'age':age[0].value,
				'gender':document.getElementsByName("gender")[0].value,
				'nf':Neck_flexion[0].value,
			    'ne':Neck_extension[0].value,
			    'kf':Knee_flexion[0].value,
			    'ke':Knee_extension[0].value,
			    'apf':plantarflexion[0].value,
			    'ad':Dorsiflexion[0].value,
			    'hf':Hip_flexion[0].value,
			    'her':Hip_external_rotators[0].value,
			    'hir':Hip_internal_rotators[0].value,
			    'ef':Elbow_flexion[0].value,
			    'ee':Elbow_extension[0].value,
			    'ser':Shoulder_external_rotation [0].value,
			    'sir':Shoulder_internal_rotation[0].value,
			};
			$.ajax({
		        url:"/jf/submit", //提交到那里
		        type:"POST", //提交类型
		        data:JSON.stringify(data_send), //提交的数据
		        success:function(data){ //success不会直接运行，当服务器有数据传输过来才会触发执行。
		　　　　	console.log('responsed data:');
		        console.log(data);
		        cm = data['compare_model'];
		        raw = data['user_raw_data'];
		        console.log(raw);
		        console.log(cm);
		        $("#nf").text("Standard value: "+ cm['nf_mean'] + ", Evaluation: " + raw['ne_eval']);
		        $("#ne").text("Standard value: "+ cm['ne_mean'] + ", Evaluation: " + raw['ne_eval']);
		        $("#kf").text("Standard value: "+ cm['kf_mean'] + ", Evaluation: " + raw['kf_eval']);
		        $("#ke").text("Standard value: "+ cm['ke_mean'] + ", Evaluation: " + raw['ke_eval']);
		        $("#apf").text("Standard value: "+ cm['apf_mean'] + ", Evaluation: " + raw['apf_eval']);
		        $("#ad").text("Standard value: "+ cm['ad_mean'] + ", Evaluation: " + raw['ad_eval']);
		        $("#hf").text("Standard value: "+ cm['hf_mean'] + ", Evaluation: " + raw['hf_eval']);
		        $("#her").text("Standard value: "+ cm['her_mean'] + ", Evaluation: " + raw['her_eval']);
		        $("#hir").text("Standard value: "+ cm['hir_mean'] + ", Evaluation: " + raw['hir_eval']);
		        $("#ef").text("Standard value: "+ cm['ef_mean'] + ", Evaluation: " + raw['ef_eval']);
		        $("#ee").text("Standard value: "+ cm['ee_mean'] + ", Evaluation: " + raw['ee_eval']);
		        $("#ser").text("Standard value: "+ cm['ser_mean'] + ", Evaluation: " + raw['ser_eval']);
		        $("#sir").text("Standard value: "+ cm['sir_mean'] + ", Evaluation: " + raw['sir_eval']);
		        
				//window.location.href = 'motionresult.html';
				var x = document.getElementById("motion_result");
				x.style.display = (x.style.display == 'none')?'block':'none';

		    	}
		    })	
		}
	}
	

}



function checkFuncvalid()
{
	if(sessionStorage.getItem("loginSuccess") != "true"){
		alert("Please login.")
		return;
	}else{
		//alert("ok");
		var age = document.getElementsByName("Age");
		var Functional_Dexterity = document.getElementsByName("Functional Dexterity");
		var Vertical_jump = document.getElementsByName("Vertical jump");
		var nine_Hole_Peg = document.getElementsByName("9 Hole Peg");
		var Stair_climb_test = document.getElementsByName("Stair climb test");
		var SEBT = document.getElementsByName("SEBT");
		var Choice_Stepping_Reaction_Time = document.getElementsByName("Choice Stepping Reaction Time");
		var Long_Jump = document.getElementsByName("Long Jump");
		var thirty_sec_sit_to_stand_test = document.getElementsByName("30-sec sit to stand test");
		var six_Minute_Walk = document.getElementsByName("6 Minute Walk");
		var Balance = document.getElementsByName("Balance");
		
		if(age[0].value ==""||isNaN(age[0].value) || age[0].value <= 0 || (age[0].value)%1!==0)
		{
		alert("Input Age Not Valid");
		}
		else if(Functional_Dexterity[0].value ==""||isNaN(Functional_Dexterity[0].value) || Functional_Dexterity[0].value <= 0){
			alert("Input Functional Dexterity Not Valid");
		}else if(Vertical_jump[0].value ==""||isNaN(Vertical_jump[0].value) || Vertical_jump[0].value < 0){
			alert("Input Vertical jump Not Valid");
		}else if(nine_Hole_Peg[0].value ==""||isNaN(nine_Hole_Peg[0].value) || nine_Hole_Peg[0].value < 0){
			alert("Input 9 Hole Peg Not Valid");
		}else if(Stair_climb_test[0].value ==""||isNaN(Stair_climb_test[0].value) || Stair_climb_test[0].value <= 0){
			alert("Input Stair climb test Not Valid");
		}else if(SEBT[0].value ==""||isNaN(SEBT[0].value) || SEBT[0].value <= 0){
			alert("Input Knee extension Not Valid");
		}else if(Choice_Stepping_Reaction_Time[0].value ==""||isNaN(Choice_Stepping_Reaction_Time[0].value) || Choice_Stepping_Reaction_Time[0].value <= 0){
			alert("Input Choice Stepping Reaction Time Not Valid");
		}else if(Long_Jump[0].value ==""||isNaN(Long_Jump[0].value) || Long_Jump[0].value <= 0){
			alert("Input Long Jump Not Valid");
		}else if(thirty_sec_sit_to_stand_test[0].value ==""||isNaN(thirty_sec_sit_to_stand_test[0].value) || thirty_sec_sit_to_stand_test[0].value <= 0){
			alert("Input30-sec sit to stand test Not Valid");
		}else if(six_Minute_Walk[0].value ==""||isNaN(six_Minute_Walk[0].value) || six_Minute_Walk[0].value <= 0){
			alert("Input 6 Minute Walk Not Valid");
		}else if(Balance[0].value ==""||isNaN(Balance[0].value) || Balance[0].value <= 0){
			alert("Input Balance Not Valid");
		}
		else {
			console.log('send data');
			data_send = {
				'age':age[0].value,
				'gender':document.getElementsByName("gender")[0].value,
			    'fdt':Functional_Dexterity[0].value,
			    'hpt9':nine_Hole_Peg[0].value,
			    'seb':SEBT[0].value,
			    'lj':Long_Jump[0].value,
			    'mwt6':six_Minute_Walk[0].value,
			    'vj':Vertical_jump[0].value,
			    'tst':Stair_climb_test[0].value,
			    'csrt':Choice_Stepping_Reaction_Time[0].value,
			    'sts':thirty_sec_sit_to_stand_test[0].value,
			    'botb':Balance[0].value,
			};
			$.ajax({
		        url:"/fp/submit", //提交到那里
		        type:"POST", //提交类型
		        data:JSON.stringify(data_send), //提交的数据
		        success:function(data){ //success不会直接运行，当服务器有数据传输过来才会触发执行。
		　　　　	console.log('responsed data:');
		        console.log(data);
		        cm = data['compare_model'];
		        raw = data['user_raw_data'];
		        console.log(raw);
		        console.log(cm);
		        $("#fdt").text("Standard value: "+ cm['fdt_mean'] + ", Evaluation: " + raw['fdt_eval']);
		        $("#hpt9").text("Standard value: "+ cm['hpt9_mean'] + ", Evaluation: " + raw['hpt9_eval']);
		        $("#seb").text("Standard value: "+ cm['seb_mean'] + ", Evaluation: " + raw['seb_eval']);
		        $("#lj").text("Standard value: "+ cm['lj_mean'] + ", Evaluation: " + raw['lj_eval']);
		        $("#mwt6").text("Standard value: "+ cm['mwt6_mean'] + ", Evaluation: " + raw['mwt6_eval']);
		        $("#vj").text("Standard value: "+ cm['vj_mean'] + ", Evaluation: " + raw['vj_eval']);
		        $("#tst").text("Standard value: "+ cm['tst_mean'] + ", Evaluation: " + raw['tst_eval']);
		        $("#csrt").text("Standard value: "+ cm['csrt_mean'] + ", Evaluation: " + raw['csrt_eval']);
		        $("#sts").text("Standard value: "+ cm['sts_mean'] + ", Evaluation: " + raw['sts_eval']);
		        $("#botb").text("Standard value: "+ cm['botb_mean'] + ", Evaluation: " + raw['botb_eval']);
		        
				//window.location.href = 'funcresult.html';
				var x = document.getElementById("func_result");
				x.style.display = (x.style.display == 'none')?'block':'none';

		    	}
		    })	
		}
	}
	

}

// perform csrf check
jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
 
    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
