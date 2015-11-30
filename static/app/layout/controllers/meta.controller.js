(function () {
  'use strict';

  angular
  .module('afya360.layout.controllers')
  .controller('MetaController', MetaController)

  MetaController.$inject = ['$scope', 'Meta'];

  function MetaController($scope, Meta) {
    var vm = this; 
    vm.pageMeta = Meta;   
  }
})();