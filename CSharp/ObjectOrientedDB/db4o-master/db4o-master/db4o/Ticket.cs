using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace db4o
{
    public class Ticket
    {
        private string change_log { get; set; }
        public DateTime closing_date { get; set; }
        public DateTime creation_date { get; set; }
        private string description { get; set; }
        private DateTime expected_update_date { get; set; }
        private string label { get; set; }
        public int priority { get; set; }
        private string subject { get; set; }
        private string unique_guid { get; set; }

        private void add_estimated_end_time()
        {
            Console.WriteLine("Estimated end time updated");
        }
        private void register_ticket()
        {
            Console.WriteLine("Ticket registered");
        }
        public void set_status()
        {
            Console.WriteLine("Status set");
        }
    }
}
