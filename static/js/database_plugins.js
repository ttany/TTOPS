$(function() {


    var uiElements = function(){

        //Datatables
        var uiDatatable = function(){
            if($("#example").length > 0){
                $('#example').DataTable( {
                    "processing": true,
                    "serverSide": true,
                    "ajax": "/system/users/data/",
                    "dom": "<'#topPlugin'>"+"t"+"<'row'<'col-sm-6'i><'col-sm-6 text-right'p>>",
                    "sort":false,
                    "columns": [
                         {
                             "sClass": "text-center",
                             "data": "id",
                             "render": function (data, type, full, meta) {
                                  return '<input class="iCheck-helper" type="checkbox" value="'+ data + '" name="id"/>';
                             },
                             "bSortable": false
                         },
                         { "data": "username" },
                         { "data": "role" },
                         { "data": "name" },
                         { "data": "tel" },
                         {
                             "data": "status",
                             "render": function (data,type,full,meta) {
                                 if(data==1){
                                     return '<span class="fa fa-check fa-lg" style="color: green"></span>';
                                 }else {
                                     return '<span class="fa fa-times fa-lg " style="color: red"></span>';
                                 }
                             }
                         },
                         {   "data": "last_login"},
                         {   "data": "id",
                             "render": function (data,type,full,meta) {
                                 if(full.status==1){
                                     return '<button id="editrow" class="btn btn-default btn-sm" value='+data+' type="button">编辑</button><button id="is_status" class="btn btn-default btn-sm" value='+data+' type="button">禁用</button>';
                                 }else {
                                     return '<button id="editrow" class="btn btn-default btn-sm" value='+data+' type="button">编辑</button><button id="is_status" class="btn btn-default btn-sm" value='+data+' type="button">启用</button>';
                                 }
                             }
                         },

                    ],

                    "language": {
                        "aria": {
                            "sortAscending": ": 以升序排列此列",
                            "sortDescending": ": 以降序排列此列"
                        },
                        "loadingRecords": "数据载入中...",
                        "emptyTable": "表中数据为空",
                        "info": "显示第 _START_ 至 _END_ 项结果，共 _TOTAL_ 项",
                        "infoEmpty": "无数据",
                        "infoFiltered": "(由 _MAX_ 项过滤得到)",
                        "infoPostFix": "",
                        "infoThousands": ",",
                        "lengthMenu": "显示 _MENU_ 项结果",
                        "search": "搜索:",
                        "zeroRecords": "没有匹配结果",
                        "paging": {
                            "first": "首页",
                            "previous": "上页",
                            "next": "下页",
                            "last": "末页"
                        },
                        "paginate": {
                            "previous": "上一页",
                            "next": "下一页",
                            "last": "尾页",
                            "first": "首页"
                        }
                    },
                } );


                $(".datatable").on('page.dt',function () {
                    onresize(100);
  
                });
            }
            
                     
        }//END Datatable        

        $(window).resize(function(){
            if($(".owl-carousel").length > 0){
                $(".owl-carousel").data('owlCarousel').destroy();
                uiOwlCarousel();
            }
        });
       
        return {
            init: function(){
                uiDatatable();

            }
        }
        
    }();

    uiElements.init();
    //全选
    $(document).on('click', 'th input:checkbox' , function(){
					var that = this;
					$(this).closest('table').find('tr > td:first-child input:checkbox')
					.each(function(){
						this.checked = that.checked;
						$(this).closest('tr').toggleClass('selected');
					});
            });

});

