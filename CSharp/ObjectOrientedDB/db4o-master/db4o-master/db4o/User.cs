using System;

/// <summary>
/// Summary description for Class1
/// </summary>
/// 
namespace db4o
{
	public abstract class User
	{
		public string Full_name { get; set; };
		public int ID { get; set; };
		public string Login { get; set; };
		private string Password { get; set; }

		public void login()
		{
			Console.WriteLine("Logged in");
		}

		public void logout()
		{
			Console.WriteLine("Logged out");
		}

		public void open_menu()
		{
			Console.WriteLine("Menu opened");
		}
	}