var temp_I = null;  //临时定时器对象
//登录按钮鼠标点击事件：用户名、密码输入初步判断
$('.panel-body button').click(function () {
    if (temp_I){   //上一次定时器未执行完
        clearInterval(temp_I);
    }
    var flag = false;   //阻止表单提交标志
    $('.form-group:lt(2) :input').each(function(){
        //如果有input输入为空
       if(!$(this).val()) {
            flag = true;   //修改标记
           var tag = $('.panel-body .errormsg');
            tag.text('用户名/密码不能为空');
            AutoHide(tag);
            return false; //退出循环
       }
    });
    //阻止表单提交
    if(flag){
        return false;
    }
});
function AutoHide(tag) {
     //定时器，错误提示一定时间后消失
    temp_I = setTimeout(function () {
        opa_var = 1;
        temp_I = setInterval(function () {
            opa_var -= 0.2;
            tag.css('opacity', opa_var);
            if (opa_var < 0) {
                clearInterval(temp_I);
                tag.empty(); //清空提示信息
                tag.css('opacity', 1);
                temp_I = null;
            }
        }, 100);
    }, 1000);
}