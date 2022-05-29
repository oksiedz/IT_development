using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace db4o
{
	public class Auditor : User
	{
		public string position { get; set; }

		void add_comment()
		{
			Console.WriteLine("Comment Added");
		}

		void add_ticket_label()
		{
			Console.WriteLine("Label Added");
		}
	}
}
