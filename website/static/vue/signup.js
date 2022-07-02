var app = new Vue({
  el: '#app',
  delimiters:['[[', ']]'],
  data: {
  	username: '',
  	f_name: '',
  	l_name: '',
  	email: '',
  	password: '',
  	errors: '',
  	message: ''
  },
  created(){

  	this.getFaqs();
  },
  methods: {
  	signUp(){
  		var vm = this;
        var url = '/account/signup/';
       	
       	var data = {
       		username: this.username,
       		f_name: this.f_name,
       		l_name: this.l_name,
       		password: this.password,
       		email: this.email,
       	}
        sendRequest(url, 'post', data)
        .then(function(response){
        	vm.errors = response.data.errors;
        	vm.message = response.data.message;
        	if (vm.message.length>1){
        		setTimeout(function(){
        			window.location.href = "/account/login/"
        		},1500)
        	}
        })
  	},
  }
})
