var app = angular.module("pasteApp", []);

app.config(['$interpolateProvider', function ($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
}]);

app.config(function ($httpProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

app.controller('DummyController', ['$scope', '$http', function ($scope, $http) {
}]);

app.filter('trusted', function($sce){
  return function(html){
    return $sce.trustAsHtml(html)
  }
});

app.controller('PasteItemCreateController', ['$scope', '$http', function ($scope, $http) {

  $scope.higlight_data = "";
  $scope.content = "";
  $scope.syntax = "";

  console.log($scope);
  $scope.$watch("content", function(newValue, oldValue) {
    if ($scope.content.length > 0) {
      $scope.test();
    }
    else {
      $scope.higlight_data = "";
    }
  });
  $scope.$watch("syntax", function(newValue, oldValue) {
    $scope.test();
  });
  $scope.$watch("is_sent_email", function(newValue, oldValue) {
    if($scope.is_sent_email) {
      $("input[name=email]").show();
    }
    else {
      $("input[name=email]").hide();
    }
  });

  $scope.test = function (data) {
    // data = data.replace("\n", "<br />")
    data = $scope.content;
    var regex = new RegExp('\n', 'g');
    data = data.replace(regex, "%0A");
    $http.get($scope.url + "?format=json&data=" + data + "&syntax_id=" + $scope.syntax)
    .success(function (response) {
      $scope.higlight_data = response.data;
    })
    .error(function (data) {
      console.log("error");
    });
  }

}]);
