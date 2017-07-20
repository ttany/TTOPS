/**
 * Created by kebz on 2017/7/6.
 */


  $(document).ready(
    function() {
      $("#inputForm").validate({
        submitHandler : function(form) {  //验证通过后的执行方法
            //当前的form通过ajax方式提交（用到jQuery.Form文件）
            $(form).ajaxSubmit({
                dataType:"json",
                success:function( jsondata ){
                    if( jsondata.code = 200 ){
                        alert("success");
                    }else{
                        alert("fail");
                    }
                  }
                });

        },
        focusInvalid : true,   //验证提示时，鼠标光标指向提示的input
        rules : {  //验证尺度
          account : {
            required : true,   //验证非空
            remote: {          //远程ajax验证
                url: "../xxxx/checkaccount", //检查是否存在账号，存在则返回true
                type: "GET",
                dataType: "json",
                data: {
                    account: function () {
                        return $("#account").val(); //这个是取要验证的用户名
                    }
                },
                dataFilter: function (data) {  //判断控制器返回的内容
                    var notice = eval("("+ data +")");
                    if( notice ){
                        return false;
                    }else{
                        return true;
                    }
                }
            }
          },
        },


      });
    });


