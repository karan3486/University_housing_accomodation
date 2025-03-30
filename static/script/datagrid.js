function InitDeleteAction() {
  debugger;
  $(".delete-button").click(function (ele) {
    debugger;
    FormDeleteSubmit(this);
  });
}

function InitEditAction() {
  $(".edit-button").click(function () {
    debugger;
    var panel_name = $(this).attr("panel-name");
    if (panel_name == "halls") {
      let id = $(this).data("id");
      RenderHallsDetail(id);
    }
    if (panel_name == "advisor") {
      let id = $(this).data("id");
      RenderAdvisorDetail(id);
    }
    if (panel_name == "houserequest") {
      let id = $(this).data("id");
      RenderHouseRequestDetail(id);
    }
    if (panel_name == "manager") {
      let id = $(this).data("id");
      RenderManagerDetail(id);
    }
    if (panel_name == "apartment") {
      let id = $(this).data("id");
      RenderApartmentDetail(id);
    }
    if (panel_name == "complain") {
      let id = $(this).data("id");
      RenderComplainDetail(id);
    }
    if (panel_name == "staff") {
      let id = $(this).data("id");
      RenderStaffDetail(id);
    }

    // window.location.href = "/registration?id=" + employeeId;
  });
}
function InitUpdateAction() {
  window.location.href = "/updateregistration";
}
function InitViewAction() {
  $(".view-button").click(function () {
    debugger;
    var email = $(this).closest("tr").find("td:eq(1)").text();
    $("#pdf-iframe").attr("src", "/view_pdf/" + email);
    $("#pdf-modal").modal("show");
  });
}

// function DataGrid() {
//   $("#employee-table").DataTable({
//     ajax: "/get_all_employees",
//     columns: [
//       { data: "name" },
//       { data: "email" },
//       { data: "country" },
//       { data: "city" },
//       { data: "zipcode" },
//       { data: "phone" },
//       { data: "department" },
//       { data: "skillpercent" },
//       {
//         data: null,
//         render: function (data, type, row) {
//           return (
//             '<button  type="button" class="button edit-button" data-id="' +
//             data.id +
//             '">Edit</button>'
//           );
//         },
//       },
//       {
//         data: null,
//         render: function (data, type, row) {
//           return (
//             '<button type="button" class="button view-button" data-id="' +
//             data.id +
//             '">View</button>'
//           );
//         },
//       },
//       {
//         data: null,
//         render: function (data, type, row) {
//           return (
//             '<button type="button" class="button delete-button" data-id="' +
//             data.id +
//             '">Delete</button>'
//           );
//         },
//       },
//     ],
//     initComplete: function () {
//       InitDeleteAction();
//       InitEditAction();
//       InitViewAction();
//       $(".paginate_button").click(function () {
//         InitDeleteAction();
//         InitEditAction();
//         InitViewAction();
//       });
//     },
//   });
// }
