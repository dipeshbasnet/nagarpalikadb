const lengthMenu = [[10, 20, 50, -1], [10, 20, 50, "All"]]
$('#business-table').DataTable({
    "lengthMenu": lengthMenu,
    "serverSide": false,
    "dom": 'T<"clear">lfrtip',
    paging: true,
    ordering: false,
    info: true,
    "ajax": {
        "serverSide": false,
        "url": listOfBusniessUrl,
        "type": "GET",
        "dataSrc": "data",
    },
    columns: [
        {"title": "Name", "data": "name"},
        {"title": "Regostration #", "data": "reg_number"},
        {"title": "Status", "data": "status"},
        {"title": "Owner", "data": "owner"},
        {"title": "Type", "data": "type"},
        {"title": "Capital", "data": "capital_amt"},
        {"title": "Ward", "data": "ward"},
        {"title": "Street", "data": "street"},
        {"title": "House #", "data": "house_no"},
    ],
    columnDefs: [
        {
            "targets": [0],
            "render": function (data, type, row, meta) {
                return data.link(businessDetailurl.replace('97987', row.uuid))
            },
        },
    ]
});