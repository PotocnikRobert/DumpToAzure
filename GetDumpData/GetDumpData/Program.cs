using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace GetDumpData
{
    class Program
    {
        static void Main(string[] args)
        {
            if ((args == null) || (args.Length != 2))
            {
                Console.WriteLine("Please provide hostname and port - DumpReader 192.168.1.1 30002"); // Check for null array
            }
            else
            {

                string hostName = args[0];
                int port = Convert.ToInt32(args[1]);
                TcpClient tcpClient = new TcpClient(hostName, port);
                NetworkStream netStream = tcpClient.GetStream();
                Byte[] data = new Byte[256];
                bool sdata = true;
                while (sdata)
                {
                    if (netStream.CanRead)
                    {
                        byte[] myReadBuffer = new byte[tcpClient.ReceiveBufferSize];
                        StringBuilder myCompleteMessage = new StringBuilder();
                        int numberOfBytesRead = 0;

                        // Incoming message may be larger than the buffer size.
                        do
                        {
                            numberOfBytesRead = netStream.Read(myReadBuffer, 0, myReadBuffer.Length);

                            myCompleteMessage.AppendFormat("{0}", Encoding.ASCII.GetString(myReadBuffer, 0, numberOfBytesRead));

                        }
                        while (netStream.DataAvailable);

                        // Print out the received message to the console.
                        //Console.WriteLine(myCompleteMessage.Length);
                        String text = myCompleteMessage.ToString();
                        text.Trim();
                        char[] delimiterChars = { ';', '*', '\n' };
                        string[] words = text.Split(delimiterChars);
                        //System.Console.WriteLine("{0} words in text:", words.Length);

                        foreach (string s in words)
                        {
                            if (s.Length != 0)
                            {
                                Console.WriteLine(s);
                            }
                        }

                        //Console.WriteLine("You received the following message : " + myCompleteMessage);
                    }
                    else
                    {
                        sdata = false;
                    }
                }

            }
        }
    }
    
}
