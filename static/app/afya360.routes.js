(function () {
  'use strict';

  angular
    .module('afya360.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider
    .when('/', {
      controller: 'HomeController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/layout/home.html'
    })
    .when('/place/:type/:slug/:id', {
      controller: 'PlaceController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/layout/home.html'
    })
    .when('/health-facility/:slug/:id', {
      controller: 'FacilityController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/facilities/facility.html'
    })
    .otherwise('/');
  }
})();